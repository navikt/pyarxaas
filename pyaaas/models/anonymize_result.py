import json
import pandas
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO


class AnonymizeResult:
    """ Collection Class for result from anonymize action"""

    def __init__(self, result_dict):
        self._result_dict = result_dict

    def to_dataframe(self):
        string_file = StringIO(self._result_dict["data"])
        return pandas.read_csv(string_file, ";")

    def to_dict(self):
        return self._result_dict


