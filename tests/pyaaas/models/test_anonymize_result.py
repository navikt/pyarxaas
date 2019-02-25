import unittest

import pandas

from pyaaas.models import anonymize_result


class AnonymizeResultTest(unittest.TestCase):

    def setUp(self):
        result_dict = {
    "anonymizeResult": {
        "data": "age,gender,zipcode\n*,male,816**\n*,female,816**\n*,male,816**\n*,female,816**\n*,male,816**\n*,female,816**\n*,male,816**\n*,female,816**\n*,male,816**\n*,female,816**\n*,male,816**\n",
        "anonymizationStatus": "ANONYMOUS",
        "payloadMetaData": {
            "sensitivityList": {
                "age": "IDENTIFYING",
                "gender": "INSENSITIVE",
                "zipcode": "INSENSITIVE"
            },
            "dataType": None,
            "hierarchy": {
                "zipcode": [
                    [
                        "81667",
                        "8166*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81668",
                        "8166*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81669",
                        "8166*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81670",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81671",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81672",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81673",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81674",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81675",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81676",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ],
                    [
                        "81677",
                        "8167*",
                        "816**",
                        "81***",
                        "8****",
                        "*****"
                    ]
                ]
            },
            "models": {
                "KANONYMITY": {
                    "k": "4"
                }
            }
        },
        "statistics": None
    },
    "beforeAnonymizationMetrics": {
        "measure_value": "[%]",
        "record_affected_by_highest_risk": "100.0",
        "sample_uniques": "0.0",
        "estimated_prosecutor_risk": "9.090909090909092",
        "population_model": "DANKAR",
        "records_affected_by_lowest_risk": "100.0",
        "estimated_marketer_risk": "9.090909090909092",
        "highest_prosecutor_risk": "9.090909090909092",
        "estimated_journalist_risk": "9.090909090909092",
        "lowest_risk": "9.090909090909092",
        "average_prosecutor_risk": "9.090909090909092",
        "population_uniques": "0.0",
        "quasi_identifiers": "[]"
    },
    "afterAnonymizationMetrics": {
        "measure_value": "[%]",
        "record_affected_by_highest_risk": "100.0",
        "sample_uniques": "0.0",
        "estimated_prosecutor_risk": "9.090909090909092",
        "population_model": "DANKAR",
        "records_affected_by_lowest_risk": "100.0",
        "estimated_marketer_risk": "9.090909090909092",
        "highest_prosecutor_risk": "9.090909090909092",
        "estimated_journalist_risk": "9.090909090909092",
        "lowest_risk": "9.090909090909092",
        "average_prosecutor_risk": "9.090909090909092",
        "population_uniques": "0.0",
        "quasi_identifiers": "[]"
    }
}
        self.test_anon_result = anonymize_result.AnonymizeResult(result_dict)

    def test_get_result_dataframe__is_pandas_dataframe(self):
        result = self.test_anon_result.get_result_dataframe()
        self.assertIsInstance(result, pandas.DataFrame, f"{result} should be instance of DataFrame")

    def test_get_metrics_before__is_pandas_dataframe(self):
        result = self.test_anon_result.get_metrics_before()
        self.assertIsInstance(result, pandas.DataFrame, f"result={type(result)} should be instance of DataFrame")

    def test_get_metrics_after__is_pandas_dataframe(self):
        result = self.test_anon_result.get_metrics_after()
        self.assertIsInstance(result, pandas.DataFrame, f"result={type(result)} should be instance of DataFrame")
