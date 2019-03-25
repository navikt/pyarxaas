import copy
from collections import Mapping

from pandas import DataFrame


class RiskProfile:

    def __init__(self, metrics: Mapping):
        self._reIdentificationOfRisk = copy.deepcopy(metrics["reIdentificationRisk"])
        self._distributionOfRisk = copy.deepcopy(metrics["distributionOfRisk"])

    def reIdentificationRisk_to_dataframe(self):
        df = DataFrame([self._reIdentificationOfRisk])
        return df

    def distributionOfRisk_to_dataframe(self):
        return DataFrame.from_dict(self._distributionOfRisk["riskIntervalList"])