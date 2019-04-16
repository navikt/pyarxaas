import copy

from pyaaas.models.anonymization_metrics import AnonymizationMetrics
from pyaaas.models.dataset import Dataset
from pyaaas.models.risk_profile import RiskProfile


class AnonymizeResult:
    """ Understands the result of a anonymization process"""

    def __init__(self, dataset: Dataset, risk_profile: RiskProfile, anonymization_metrics: AnonymizationMetrics, anonymization_status):
        self._anonymization_metrics = anonymization_metrics
        self._risk_profile = risk_profile
        self._dataset = dataset
        self._anonymization_status = anonymization_status

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(hash(self._anonymization_metrics) + hash(self._risk_profile) + hash(self._dataset))

    @property
    def dataset(self) -> Dataset:
        """
        Dataset created from the anonymization

        :return: Dataset
        """
        return copy.deepcopy(self._dataset)

    @property
    def risk_profile(self) -> RiskProfile:
        """
        RiskProfile asscocciated with the new Dataset

        :return: RiskProfile
        """
        return copy.deepcopy(self._risk_profile)

    @property
    def anonymization_metrics(self) -> AnonymizationMetrics:
        """
        AnonymizationMetrics about the anonymization process.
        Contains data on hierarchy level used and privacy model configuration

        :return: AnonymizationMetrics
        """
        return copy.deepcopy(self._anonymization_metrics)

    @property
    def anonymization_status(self) -> str:
        """
        Anonymization status for the new Dataset

        :return: str
        """
        return self._anonymization_status

    @classmethod
    def _from_response(cls, dataset, risk_profile, anon_metrics, anon_status):
        anonymize_metrics = AnonymizationMetrics(anon_metrics)
        return cls(dataset, risk_profile, anonymize_metrics, anon_status)



