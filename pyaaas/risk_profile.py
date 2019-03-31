import copy
from collections import Mapping

from pandas import DataFrame


class RiskProfile:

    def __init__(self, metrics: Mapping):
        self._re_identification_of_risk = copy.deepcopy(metrics["reIdentificationRisk"])
        self._distribution_of_risk = copy.deepcopy(metrics["distributionOfRisk"])

    @property
    def re_identification_risk(self):
        return copy.deepcopy(self._re_identification_of_risk["measures"])

    @property
    def distribution_of_risk(self):
        return copy.deepcopy(self.distribution_of_risk)

    def re_identification_risk_dataframe(self):
        df = DataFrame([self._re_identification_of_risk["measures"]])
        return df

    def distribution_of_risk_dataframe(self):
        return DataFrame.from_dict(self._distribution_of_risk["riskIntervalList"])