import copy

from pyaaas.hierarchy.grouping_based_hierarchy import GroupingBasedHierarchy
from pyaaas.hierarchy.interval_builder.interval import Interval


class IntervalHierarchyBuilder(GroupingBasedHierarchy):
    """
    Represents a specific strategy for creating a value generalization hierarchy
    """

    def __init__(self):
        super().__init__()
        self._intervals = {}

    @property
    def intervals(self):
        return list(copy.deepcopy(self._intervals))

    def add_interval(self, from_n, to_n, label: str=None):
        """
        Add a interval to the builder. from_n is inclusive, to_n is exclusive

        :param from_n: create interval inclusive from this value
        :param to_n: create interval to this value
        :param label: (optional) set a string label for the interval
        :return: None

        """
        # using dict to enforce uniqueness and order
        self._intervals[Interval(from_n, to_n, label)] = ""

    def _request_payload(self):
        return {
            "builder": {
                "type": "intervalBased",
                "dataType": self._data_type(),
                "intervals": [interval.payload() for interval in self._intervals.keys()],
                "levels": [level.payload() for level in self.levels]
            }
        }

    def _data_type(self):
        for interval in self._intervals:
            if interval.is_decimal():
                return "DOUBLE"
        return "LONG"

    @staticmethod
    def _is_decimal(number):
        return "." in number
