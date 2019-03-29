import copy
from collections import Mapping

from pandas import DataFrame


class RiskProfile:

    def __init__(self, metrics: Mapping):
        self._re_identification_of_risk = copy.deepcopy(metrics["reIdentificationRisk"])
        self._distribution_of_risk = copy.deepcopy(metrics["distributionOfRisk"])

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self._metric_hash(self._re_identification_of_risk)
                    + self._metric_hash(self._distribution_of_risk["riskIntervalList"][0]))

    def _metric_hash(self, metric):
        m_hash = hash("")
        for metric, value in metric.items():
            m_hash = hash(m_hash + hash(hash(metric) + hash(str(value))))
        return m_hash


    @property
    def re_identification_risk(self):
        return copy.deepcopy(self._re_identification_of_risk)

    @property
    def distribution_of_risk(self):
        return copy.deepcopy(self._distribution_of_risk)

    def re_identification_risk_dataframe(self):
        df = DataFrame([self._re_identification_of_risk])
        return df

    def distribution_of_risk_dataframe(self):
        return DataFrame.from_dict(self._distribution_of_risk["riskIntervalList"])
