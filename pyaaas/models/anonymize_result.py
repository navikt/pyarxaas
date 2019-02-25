import json
import pandas
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from pyaaas import converters


class AnonymizeResult:
    """ Collection Class for result from anonymize action"""

    CSV_SEPARATOR = ","

    def __init__(self, result_dict):
        self._result_dict = result_dict

    def get_result_dataframe(self):
        """
        Returns the anonymized data

        :return: pandas.DataFrame containing the anonymized data
        """
        string_file = StringIO(self._result_dict["anonymizeResult"]["data"])
        return pandas.read_csv(string_file, self.CSV_SEPARATOR)

    def get_metrics_before(self):
        """
        Returns the anonymization metrics for the data before anonymization

        :return: pandas.DataFrame containing the metrics for the data before anonymization
        """

        metrics = self._result_dict["beforeAnonymizationMetrics"]
        return converters.create_dataframe_with_index_from_mapping(metrics, columns=("metric", "value"))

    def get_metrics_after(self):
        """
        Returns the anonymization metrics for the anonymized data

        :return: pandas.DataFrame containing the metrics for the anonymized data
        """
        metrics = self._result_dict["afterAnonymizationMetrics"]
        return converters.create_dataframe_with_index_from_mapping(metrics, columns=("metric", "value"))

    def to_dict(self):
        return self._result_dict


