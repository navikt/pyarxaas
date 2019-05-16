import copy
from collections import Mapping

from pandas import DataFrame


class RiskProfile:
    """
    Represents the re-identification risks associated with a Dataset
    """

    def __init__(self, metrics: Mapping):
        self._re_identification_of_risk = copy.deepcopy(metrics["reIdentificationRisk"]["measures"])
        self._distribution_of_risk = copy.deepcopy(metrics["distributionOfRisk"])
        self._attacker_success_rate = copy.deepcopy(metrics["reIdentificationRisk"]["attackerSuccessRate"]["successRates"])
        self._quasi_identifiers = metrics["reIdentificationRisk"]["quasiIdentifiers"]
        self._population_model = metrics["reIdentificationRisk"]["populationModel"]

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
        """
        Re-identification risk metrics for a given Dataset

        :return: dict containing re-identification metrics
        """
        return copy.deepcopy(self._re_identification_of_risk)

    @property
    def distribution_of_risk(self):
        """
        Distribution of risk for a given Dataset

        :return: dict containing the distribution of risks in a given Dataset
        """
        return copy.deepcopy(self._distribution_of_risk)

    @property
    def attacker_success_rate(self):
        """
        Attacker success rates against re-identification for a given Dataset

        :return: dict containing the attacker success rate.
        """
        return copy.deepcopy(self._attacker_success_rate)

    @property
    def quasi_identifiers(self):
        """
        Quasi-identifiers for a given Dataset

        :return: dict containing a list of all the quasi-identifying attribute in a a given Dataset
        """
        return copy.deepcopy(self._quasi_identifiers)

    @property
    def population_model(self):
        """
        Population model used to analyze a given Dataset

        :return: The Population model name used to analyze a given Dataset
        """
        return self._population_model

    def re_identification_risk_dataframe(self) -> DataFrame:
        """
        Re-identification risk as a pandas.DataFrame

        :return: pandas.Dataframe with risk metrics
        """
        df = DataFrame([self._re_identification_of_risk])
        return df

    def distribution_of_risk_dataframe(self) -> DataFrame:
        """
        Distribution of risk as a pandas.DataFrame

        :return: pandas.DataFrame
        """
        return DataFrame.from_dict(self._distribution_of_risk["riskIntervalList"])
