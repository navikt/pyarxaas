import unittest
from pyaaas.models.anonymization_metrics import AnonymizationMetrics
from tests.pyaaas import data_generator


class AnonymizationMetricsTest(unittest.TestCase):

    def setUp(self):
        self.test_metrics = data_generator.raw_anonymization_metrics()

    def test_init(self):
       self.assertIsNotNone(AnonymizationMetrics(self.test_metrics))

    def test_elapsed_time(self):
        am = AnonymizationMetrics(self.test_metrics)
        actual = self.test_metrics["processTimeMillisecounds"]
        self.assertEqual(actual, am.elapsed_time)

    def test_privacy_models(self):
        am = AnonymizationMetrics(self.test_metrics)
        self.assertEqual(self.test_metrics["privacyModels"], am.privacy_models)
        self.assertIsNot(self.test_metrics["privacyModels"], am.privacy_models)

    def test_attribute_generalization(self):
        am = AnonymizationMetrics(self.test_metrics)
        self.assertEqual(self.test_metrics["attributeGeneralization"], am.attribute_generalization)
        self.assertIsNot(self.test_metrics["attributeGeneralization"], am.attribute_generalization)

    def test_equality(self):
        am1 = AnonymizationMetrics(self.test_metrics)
        am2 = AnonymizationMetrics(self.test_metrics)
        self.assertEqual(am1, am2)
        self.assertIsNot(am1, am2)
        am2._elapsed_time = 200
        self.assertNotEqual(am1, am2)

    def test_hashcode(self):
        am1 = AnonymizationMetrics(self.test_metrics)
        am2 = AnonymizationMetrics(self.test_metrics)
        test_set = {am1, am2}
        self.assertEqual(1, len(test_set))
