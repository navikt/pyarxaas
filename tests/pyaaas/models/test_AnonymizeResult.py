import unittest

from models.anonymize_result import AnonymizeResult
from models.dataset import Dataset
from tests.pyaaas import data_generator


class AnonymizeResultTest(unittest.TestCase):

    def setUp(self):
        self.test_dataset = data_generator.id_name_dataset()
        self.test_risk_profile = data_generator.risk_profile()
        self.test_anoymization_metrics = data_generator.anonymization_metrics()
        self.test_anon_metrics = self.test_anoymization_metrics.metrics

    def test_init(self):
        AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)

    def test_equaltiy(self):
        ar1 = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        ar2 = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        self.assertEqual(ar1, ar2)
        ar2._dataset = Dataset([["data", "data2"]])
        self.assertNotEqual(ar1, ar2)

    def test_hash(self):
        ar1 = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        ar2 = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        test_set = {ar1, ar2}
        self.assertEqual(1, len(test_set))

    def test_dataset(self):
        ar = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        dataset = ar.dataset
        self.assertIsNotNone(dataset)
        self.assertEqual(self.test_dataset, dataset)

    def test_risk_profile(self):
        ar = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        risk_profile = ar.risk_profile
        self.assertIsNotNone(risk_profile)
        self.assertEqual(self.test_risk_profile, risk_profile)

    def test_anonymization_metrics(self):
        ar = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        anonymization_metrics = ar.anonymization_metrics
        self.assertIsNotNone(anonymization_metrics)
        self.assertEqual(self.test_anoymization_metrics, anonymization_metrics)

    def test_create_from_response_payload(self):
        ar1 = AnonymizeResult._from_response(self.test_dataset, self.test_risk_profile, self.test_anon_metrics)
        ar2 = AnonymizeResult(self.test_dataset, self.test_risk_profile, self.test_anoymization_metrics)
        self.assertEqual(ar1, ar2)

