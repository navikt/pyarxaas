import unittest

from pandas import DataFrame

from pyaaas.risk_profile import RiskProfile


class RiskProfileTest(unittest.TestCase):

    def setUp(self):
        self.test_metric = {"metrics": {
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

    def test_init(self):
        RiskProfile(self.test_metric)

    def test_to_dataframe(self):
        risk_profile = RiskProfile(self.test_metric)
        df = risk_profile.to_dataframe()
        self.assertIsInstance(df, DataFrame)

    def test_to_dataframme_shape(self):
        risk_profile = RiskProfile(self.test_metric)
        df = risk_profile.to_dataframe()
        self.assertEqual(self.test_metric["metrics"]["records_affected_by_highest_risk"], df["records_affected_by_highest_risk"][0])