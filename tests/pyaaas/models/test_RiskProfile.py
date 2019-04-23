import json
import unittest
from pathlib import Path

from numpy import dtype
from pandas import DataFrame

from pyaaas.models.risk_profile import RiskProfile


class RiskProfileTest(unittest.TestCase):

    def setUp(self):
        response_path = Path(__file__).parent.joinpath("..").joinpath("test_data").joinpath("analyze_response_test_data.json")
        with response_path.open(encoding="utf-8") as file:
            json_str = file.read()
        self.risk_profile_response = json.loads(json_str)

    def test_init(self):
        RiskProfile(self.risk_profile_response)

    def test_equality(self):
        risk_profile_1 = RiskProfile(self.risk_profile_response)
        risk_profile_2 = RiskProfile(self.risk_profile_response)
        self.assertEqual(risk_profile_1, risk_profile_2)
        risk_profile_2._re_identification_of_risk["estimated_prosecutor_risk"] = 50.0
        self.assertNotEqual(risk_profile_1, risk_profile_2)

    def test_hash(self):
        risk_profile_1 = RiskProfile(self.risk_profile_response)
        risk_profile_2 = RiskProfile(self.risk_profile_response)
        test_set = {risk_profile_1, risk_profile_2}
        self.assertEqual(1, len(test_set))

    def test_to_dataframe(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertIsInstance(df, DataFrame)

    def test_re_identification_risk_to_dataframe_shape(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.re_identification_risk_dataframe()
        self.assertEqual(self.risk_profile_response["reIdentificationRisk"]["measures"]["records_affected_by_highest_prosecutor_risk"], df["records_affected_by_highest_prosecutor_risk"][0])

    def test_distribution_of_risk_to_dataframe_shape(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.distribution_of_risk_dataframe()
        self.assertEqual(self.risk_profile_response["distributionOfRisk"]["riskIntervalList"][0]["interval"],
                         df["interval"][0])

    def test_re_identification_risk_to_dataframe__column_types(self):
        risk_profile = RiskProfile(self.risk_profile_response)
        df = risk_profile.re_identification_risk_dataframe()
        for d_type in df.dtypes.tolist():
            self.assertEqual(d_type, dtype("float64"))

    def test_attacker_success_rate_property(self):
        expected = {'Prosecutor_attacker_success_rate': 1.0, 'Marketer_attacker_success_rate': 1.0, 'Journalist_attacker_success_rate': 1.0}
        risk_profile = RiskProfile(self.risk_profile_response)
        self.assertEqual(expected, risk_profile.attacker_success_rate)

    def test_quasi_indentifers_property(self):
        expected = ['zipcode']
        risk_profile = RiskProfile(self.risk_profile_response)
        self.assertEqual(expected, risk_profile.quasi_identifiers)

    def test_population_model_property(self):
        expected = "ZAYATZ"
        risk_profile = RiskProfile(self.risk_profile_response)
        self.assertEqual(expected, risk_profile.population_model)
