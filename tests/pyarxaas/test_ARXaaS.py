import json
import unittest

from uplink import Body

from pyarxaas.hierarchy import RedactionHierarchyBuilder
from pyarxaas.arxaas_connector import ARXaaSConnector
from pyarxaas.privacy_models import KAnonymity
from pyarxaas.arxaas import ARXaaS
from pyarxaas.models.anonymize_result import AnonymizeResult
from pyarxaas.models.attribute_type import AttributeType
from pyarxaas.models.dataset import Dataset
from tests.pyarxaas import data_generator


class AnalyzationResponseStub:

    @property
    def text(self):
        return json.dumps(data_generator.analyze_response())

    @property
    def status_code(self):
        return 200


class AnonymzationResponseStub:

    @property
    def text(self):
        return json.dumps(data_generator.anonymize_response())

    @property
    def status_code(self):
        return 200


class HierarchyResponseStub:

    @property
    def text(self):
        return '{"hierarchy":[["1123","*123","**23","***3","****"],["1321","*321","**21","***1","****"],["1234",' \
               '"*234","**34","***4","****"],["1532","*532","**32","***2","****"]]} '

    @property
    def status_code(self):
        return 200


class RootResponseStub:

    @property
    def text(self):
        return '{"_links": {_self: "test"}}'

    @property
    def status_code(self):
        return 200


class MockAaasConnector(ARXaaSConnector):

    def anonymize_data(self, payload: Body):
        return AnonymzationResponseStub()

    def risk_profile(self, payload: Body):
        return AnalyzationResponseStub()

    def hierarchy(self, payload: Body):
        return HierarchyResponseStub()

    def root(self):
        return RootResponseStub()


class ARXaaSTest(unittest.TestCase):

    def setUp(self):
        self.test_data = [['id', 'name'],
                          ['0', 'Viktor'],
                          ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

        self.test_dataset = Dataset(self.test_data, self.test_attribute_type_mapping)

        self.test_raw_analyze_response = data_generator.analyze_response()
        self.test_raw_anon_response = data_generator.anonymize_response()

    def test_init(self):
        ARXaaS('http://localhost', connector=MockAaasConnector)

    def test_analyze(self):
        aaas = ARXaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.risk_profile(self.test_dataset))

    def test_anaonymize(self):
        aaas = ARXaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.anonymize(self.test_dataset, privacy_models=[KAnonymity(4)]))

    def test_risk_profile_return_value(self):
        aaas = ARXaaS('http://localhost', connector=MockAaasConnector)
        risk_profile = aaas.risk_profile(self.test_dataset)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertEqual(self.test_raw_analyze_response["reIdentificationRisk"]["measures"][
                             "records_affected_by_highest_prosecutor_risk"],
                         df["records_affected_by_highest_prosecutor_risk"][0])

    def test_anonymize_return_value(self):
        aaas = ARXaaS('http://localhost', connector=MockAaasConnector)
        anonymized_dataset = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertIsInstance(anonymized_dataset, AnonymizeResult)

    def test_anonymize__dataset_attributes_are_correct(self):
        aaas = ARXaaS('http://localhost', connector=MockAaasConnector)
        anonymize_result = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertEqual(AttributeType.IDENTIFYING, AttributeType(anonymize_result.dataset._attributes[0].type))

    def test_redaction_based_hierarchy(self):
        expected = [["1123", "*123", "**23", "***3", "****"], ["1321", "*321", "**21", "***1", "****"],
                    ["1234", "*234", "**34", "***4", "****"], ["1532", "*532", "**32", "***2", "****"]]
        aaas = ARXaaS('http://localhost:8080', connector=MockAaasConnector)
        redaction_builder = RedactionHierarchyBuilder(
            " ",
            "*",
            RedactionHierarchyBuilder.Order.RIGHT_TO_LEFT,
            RedactionHierarchyBuilder.Order.LEFT_TO_RIGHT)
        column = ["1123", "1321", "1234", "1532"]
        hierarchy = aaas.hierarchy(redaction_builder, column)
        self.assertEqual(expected, hierarchy)
