import unittest
from pyaaas.anonymization_metrics import AnonymizationMetrics

class AnonymizationMetricsTest(unittest.TestCase):

    def setUp(self):
        self.test_metrics = {
            "attributeGeneralization": [
                {
                    "name": "age",
                    "type": "QUASI_IDENTIFYING_ATTRIBUTE",
                    "generalizationLevel": 1
                },
                {
                    "name": "gender",
                    "type": "QUASI_IDENTIFYING_ATTRIBUTE",
                    "generalizationLevel": 0
                },
                {
                    "name": "zipcode",
                    "type": "QUASI_IDENTIFYING_ATTRIBUTE",
                    "generalizationLevel": 2
                }
            ],
            "processTimeMillisecounds": 21,
            "privacyModels": [
                {
                    "monotonicWithGeneralization": True,
                    "k": 3,
                    "riskThresholdJournalist": 0.3333333333333333,
                    "riskThresholdMarketer": 0.3333333333333333,
                    "riskThresholdProsecutor": 0.3333333333333333,
                    "localRecodingSupported": True,
                    "requirements": 1,
                    "minimalClassSizeAvailable": True,
                    "minimalClassSize": 3,
                    "populationModel": None,
                    "subset": None,
                    "sampleBased": False,
                    "subsetAvailable": False,
                    "dataSubset": None,
                    "monotonicWithSuppression": True
                }
            ]

        }
    def test_init(self):

       self.assertIsNotNone(AnonymizationMetrics(self.test_metrics))
