import copy
import json
import unittest

from uplink import Body

from pyaaas.aaas_connector import AaaSConnector
from pyaaas.privacy_models import KAnonymity
from pyaaas.aaas import AaaS
from pyaaas.models.anonymize_result import AnonymizeResult
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.dataset import Dataset
from tests.pyaaas import data_generator


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


class MockAaasConnector(AaaSConnector):

    def anonymize_data(self, payload: Body):
        return AnonymzationResponseStub()

    def risk_profile(self, payload: Body):
        return AnalyzationResponseStub()


class AaaSTest(unittest.TestCase):

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
        AaaS('http://localhost')
        
    def test_analyze(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.risk_profile(self.test_dataset))

    def test_anaonymize(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.anonymize(self.test_dataset, privacy_models=[KAnonymity(4)]))

    def test_risk_profile_return_value(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        risk_profile = aaas.risk_profile(self.test_dataset)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertEqual(self.test_raw_analyze_response["reIdentificationRisk"]["measures"]["records_affected_by_highest_prosecutor_risk"], df["records_affected_by_highest_prosecutor_risk"][0])

    def test_anonymize_return_value(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        anonymized_dataset = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertIsInstance(anonymized_dataset, AnonymizeResult)

    def test_anonymize__dataset_attributes_are_correct(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        anonymize_result = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertEqual(AttributeType.IDENTIFYING, AttributeType(anonymize_result.dataset._attributes[0].type))
