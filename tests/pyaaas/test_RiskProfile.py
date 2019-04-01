import unittest

from pandas import DataFrame

from pyaaas.risk_profile import RiskProfile


class RiskProfileTest(unittest.TestCase):

    def setUp(self):
        self.risk_profile_response = {"reIdentificationRisk": {"measures": {
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
        }},
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

    def test_init(self):
        RiskProfile(self.risk_profile_response)

    def test_equality(self):
        risk_profile_1 = RiskProfile(self.test_metric)
        risk_profile_2 = RiskProfile(self.test_metric)
        self.assertEqual(risk_profile_1, risk_profile_2)
        risk_profile_2._re_identification_of_risk["estimated_prosecutor_risk"] = "50.0"
        self.assertNotEqual(risk_profile_1, risk_profile_2)

    def test_hash(self):
        risk_profile_1 = RiskProfile(self.test_metric)
        risk_profile_2 = RiskProfile(self.test_metric)
        test_set = {risk_profile_1, risk_profile_2}
        self.assertEqual(1, len(test_set))

    def test_to_dataframe(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertIsInstance(df, DataFrame)

    def test_reIdentificationRisk_to_dataframe_shape(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertEqual(self.risk_profile_response["reIdentificationRisk"]["measures"]["records_affected_by_highest_prosecutor_risk"], df["records_affected_by_highest_prosecutor_risk"][0])

    def test_distributionOfRisk_to_dataframe_shape(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.distribution_of_risk_dataframe()
        self.assertEqual(self.risk_profile_response["distributionOfRisk"]["riskIntervalList"][0]["interval"],
                         df["interval"][0])