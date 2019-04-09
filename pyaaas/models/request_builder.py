import copy
from collections.abc import Mapping, Sequence

from pyaaas.models.privacy_models import PrivacyModel
from pyaaas.models.dataset import Dataset


class RequestBuilder:
    """
    Builds JSON serializable mappings from Dataset and PrivacyModels
    """

    def __init__(self, dataset: Dataset):
        self._dataset = dataset
        self._privacy_models = []

    def add_privacy_model(self, privacy_model: PrivacyModel):
        self._privacy_models.append(privacy_model)
        return self

    def add_privacy_models(self, privacy_models: Sequence):
        self._privacy_models += privacy_models
        return self

    def build_analyze_request(self):
        data_dict = self._dataset._payload()
        self._strip_hierarchies(data_dict)
        return data_dict

    def build_anonymize_request(self) -> Mapping:
        """
        Creates a anonymize payload to be sent to the backend

        :param dataset: Dataset to be anonymized
        :param privacy_models: privacy models to be used in the anonymization
        :return: Mapping payload
        """
        data_dict = self._dataset._payload()
        models = []
        for model in self._privacy_models:
            models.append(model._payload())
        data_dict["privacyModels"] = models
        return data_dict

    def _strip_hierarchies(self, data_dict) -> None:
        attributes = data_dict["attributes"]
        for attribute in attributes:
            del attribute["hierarchy"]



