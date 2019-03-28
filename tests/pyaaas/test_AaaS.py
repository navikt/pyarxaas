import copy
import json
import unittest

from uplink import Body

from pyaaas.aaas_connector import AaaSConnector
from pyaaas import KAnonymity
from pyaaas.aaas import AaaS
from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset

test_metrics = {"reIdentificationRisk": {
            "measure_value": "[%]",
            "Prosecutor_attacker_success_rate": "98.72",
            "records_affected_by_highest_prosecutor_risk": "97.46000000000001",
            "sample_uniques": "97.46000000000001",
            "estimated_prosecutor_risk": "100.0",
            "population_model": "PITMAN",
            "highest_journalist_risk": "100.0",
            "records_affected_by_lowest_risk": "0.06",
            "estimated_marketer_risk": "98.72000000000001",
            "Journalist_attacker_success_rate": "98.72",
            "highest_prosecutor_risk": "100.0",
            "estimated_journalist_risk": "100.0",
            "lowest_risk": "33.33333333333333",
            "Marketer_attacker_success_rate": "98.72",
            "average_prosecutor_risk": "98.72000000000001",
            "records_affected_by_highest_journalist_risk": "97.46000000000001",
            "population_uniques": "39.64593493418713",
            "quasi_identifiers": ["Innvandrerbakgrunn", "Ytelse", "Innsatsgruppe", "Ledighetsstatus"]
        },
            "distributionOfRisk": {"riskIntervalList": [{"interval": "]50,100]",
                       "recordsWithRiskWithinInteval": 0.9746,
                       "recordsWithMaxmalRiskWithinInterval": 1.0},
                      {"interval": "]33.4,50]",
                       "recordsWithRiskWithinInteval": 0.0248,
                       "recordsWithMaxmalRiskWithinInterval": 0.0254},
                      {"interval": "]25,33.4]",
                       "recordsWithRiskWithinInteval": 0.0006,
                       "recordsWithMaxmalRiskWithinInterval": 0.0006},
                      {"interval": "]20,25]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]16.7,20]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]14.3,16.7]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]12.5,14.3]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]10,12.5]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]9,10]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]8,9]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]7,8]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]6,7]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]5,6]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]4,5]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]3,4]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]2,3]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]1,2]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]0.1,1]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]0.01,0.1]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]0.001,0.01]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]0.0001,0.001]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]1e-5,0.0001]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]1e-6,1e-5]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0},
                      {"interval": "]0,1e-6]",
                       "recordsWithRiskWithinInteval": 0.0,
                       "recordsWithMaxmalRiskWithinInterval": 0.0}]
            }

        }

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
        df = risk_profile.re_identification_risk_dataframe()
        self.assertEqual(self.test_metrics_dict["reIdentificationRisk"]["records_affected_by_highest_prosecutor_risk"], df["records_affected_by_highest_prosecutor_risk"][0])

    def test_anonymize_return_value(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        anonymized_dataset = aaas.anonymize(self.test_dataset, [KAnonymity(4)])
        self.assertIsInstance(anonymized_dataset, Dataset)