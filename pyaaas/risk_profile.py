import copy
from collections import Mapping

from pandas import DataFrame


class RiskProfile:

    def __init__(self, metrics: Mapping):
        self._metrics = copy.deepcopy(metrics["metrics"])

    def to_dataframe(self):
        df = DataFrame([self._metrics])
        return df