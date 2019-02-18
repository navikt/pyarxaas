import unittest

import pandas

from pyaaas.models import anonymize_result


class AnonymizeResultTest(unittest.TestCase):

    def setUp(self):
        result_dict = {"data": "field1;field2;\n"
                               "row1field1;row1field2\n"
                               "row2field2;row2;field2",
                       "metrics_before": {"test_metric": "test_value"},
                       "metrics_after": {"test_metric": "test_value"}}
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
