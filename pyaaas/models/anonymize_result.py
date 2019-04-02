import copy

from models.anonymization_metrics import AnonymizationMetrics
from models.dataset import Dataset
from models.risk_profile import RiskProfile


class AnonymizeResult:
    """ Understands the result of a anonymization process"""

    def __init__(self, dataset: Dataset, risk_profile: RiskProfile, anonymization_metrics: AnonymizationMetrics):
        self._anonymization_metrics = anonymization_metrics
        self._risk_profile = risk_profile
        self._dataset = dataset

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(hash(self._anonymization_metrics) + hash(self._risk_profile) + hash(self._dataset))

    @property
    def dataset(self):
        return copy.deepcopy(self._dataset)

    @property
    def risk_profile(self):
        return copy.deepcopy(self._risk_profile)

    @property
    def anonymization_metrics(self):
        return copy.deepcopy(self._anonymization_metrics)

    @classmethod
    def _from_response(cls, dataset, risk_profile, anon_metrics):
        anonymize_metrics = cls.AnonymizationMetrics(anon_metrics)
        return cls(dataset, risk_profile, anonymize_metrics)



