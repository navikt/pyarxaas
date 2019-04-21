import copy

from pyaaas.models.hierarchy.interval_builder.level import Level
from pyaaas.models.hierarchy.interval_builder.interval import Interval


class IntervalHierarchyGenerator:
    """
    Represents a specific strategy for creating a value generalization hierarchy
    """

    def __init__(self):
        self._levels = []
        self._intervals = set()
        self._level_count = 0
        self._column = None

    @property
    def intervals(self):
        return list(copy.deepcopy(self._intervals))

    @property
    def levels(self):
        return copy.deepcopy(self._levels)

    def add_interval(self, from_, to, label: str=None):
        """
        Add a interval to the builder
        from_ is inclusive, to is exclusive

        :param from_: create interval with and from this value
        :param to: create interval to this value
        :param label: (optional) set a string label for the interval
        :return: None

        """
        self._intervals.add(Interval(from_, to, label))

    def level(self, level) -> Level:
        """
        Get a level in the hierarchy

        :param level: int representing the level
        :return: Level
        """
        if level > self._level_count:
            raise AttributeError(f"level={level} is higher than available levels={self._level_count}")
        if level == len(self._levels):
            self._level_count += 1
            self._levels.append(Level(level))
        return self._levels[level]

    def prepare(self, column):
        self._column = column

    def _request_payload(self):
        return {
            "column": self._column,
            "builder": {
                "type": "intervalBased",
                "intervals": [interval.payload() for interval in self._intervals],
                "levels": [level.payload() for level in self._levels]
            }
        }
