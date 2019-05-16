import copy
from collections.abc import Mapping


class AnonymizationMetrics:
    """ Understand metrics from a anonymization process"""

    def __init__(self, metrics: Mapping):
        self._elapsed_time = self._fetch_elapsed_time(metrics)
        self._attribute_generalization = self._fetch_attribute_generalization(metrics)
        self._privacy_models = self._fetch_privacy_models(metrics)

    def _fetch_elapsed_time(self, metrics):
        return metrics["processTimeMillisecounds"]

    def _fetch_attribute_generalization(self, metrics):
        return metrics["attributeGeneralization"]

    def _fetch_privacy_models(self, metrics):
        return metrics["privacyModels"]

    @property
    def attribute_generalization(self):
        """
        Property for getting the attribute generalization

        :return: Returns a dict containing all the quasi-identifying attributes and the transformation level used to anonymize the dataset.
        """
        return copy.deepcopy(self._attribute_generalization)

    @property
    def privacy_models(self):
        """
        Property for getting the privacy models with the configurations used in the anonymization process.

        :return: Returns a dict containing all the privacy models with the configuration used.
        """
        return copy.deepcopy(self._privacy_models)

    @property
    def elapsed_time(self):
        """
        Property for getting the elapsed time for the anonymization process

        :return: Returns the elapsed time in miliseconds
        """
        return self._elapsed_time

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        am_hash = hash(self.elapsed_time)
        for list_of_maps in (self._privacy_models, self._attribute_generalization):
            am_hash = hash(am_hash + self._hash_from_list_with_map(list_of_maps))
        return am_hash

    def _hash_from_list_with_map(self, list_of_items):
        am_hash = hash("")
        for mapping in list_of_items:
            am_hash = hash(am_hash + self._hash_from_mapping(mapping))
        return am_hash

    def _hash_from_mapping(self, mapping):
        am_hash = hash("")
        for metric, value in mapping.items():
            am_hash = hash(am_hash + hash(metric) + hash(str(value)))
        return am_hash



