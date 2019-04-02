import copy
from collections.abc import Mapping

class AnonymizationMetrics:
    """ Understands metrics from a anonymization process"""

    def elapsed_time_parse(self):
        return self._metrics.get("processTimeMillisecounds")

    def attribute_generalization_parse(self):
        print(self._metrics)
        return self._metrics["attributeGeneralization"]

    def __init__(self, metrics: Mapping):
        self._metrics = metrics
        self.elapsed_time = self.elapsed_time_parse()
        self._attribute_generalization = self.attribute_generalization_parse()



    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        am_hash = hash("")
        for metric, value in self._metrics.items():
            am_hash = hash(am_hash + hash(metric) + hash(str(value)))
        return am_hash

    @property
    def attribute_generalization(self):
        return copy.deepcopy(self._attribute_generalization)
