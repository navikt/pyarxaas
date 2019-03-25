import copy
import json
import unittest

from uplink import Body

from pyaaas.aaas_connector import AaaSConnector
from pyaaas import KAnonymity
from pyaaas.aaas import AaaS
from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset

test_metrics = {"metrics": {
            "measure_value": "[%]",
            "records_affected_by_highest_risk": "2.8000000000000003",
             "sample_uniques": "2.8000000000000003",
            "estimated_prosecutor_risk": "100.0",
             "population_model": "PITMAN",
            "records_affected_by_lowest_risk": "15.620000000000001",
             "estimated_marketer_risk": "12.06",
            "highest_prosecutor_risk": "100.0",
             "estimated_journalist_risk": "100.0",
            "lowest_risk": "0.4878048780487805",
             "average_prosecutor_risk": "12.06",
            "population_uniques": "0.042243729241281044",
             "quasi_identifiers": ["Innvandrerbakgrunn", "Ytelse", "Innsatsgruppe", "Ledighetsstatus"]
        }}

test_anon_response = {"anonymizeResult": {
        "data": [["name", "id"], ["lars", "0"]]
    }}

class MockResponse:

    @property
    def text(self):
        return json.dumps(test_metrics)

    @property
    def status_code(self):
        return 200

class MockAnonymzationResponse:

    @property
    def text(self):
        return json.dumps(test_anon_response)

    @property
    def status_code(self):
        return 200

class MockAaasConnector(AaaSConnector):

    def anonymize_data(self, payload: Body):
        return MockAnonymzationResponse()

    def risk_profile(self, payload: Body):
        return MockResponse()


class AaaSTest(unittest.TestCase):

    def setUp(self):
        self.test_data = [['id', 'name'],
                         ['0', 'Viktor'],
                         ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

        self.test_dataset = Dataset(self.test_data, self.test_attribute_type_mapping)

        self.test_metrics_dict = copy.deepcopy(test_metrics)
        self.test_anon_response = copy.deepcopy(test_anon_response)

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
        df = risk_profile.to_dataframe()
        self.assertEqual(self.test_metrics_dict["metrics"]["records_affected_by_highest_risk"], df["records_affected_by_highest_risk"][0])

    def test_anonymize_return_value(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        anonymized_dataset = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertIsInstance(anonymized_dataset, Dataset)