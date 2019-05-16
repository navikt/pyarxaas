import copy
from abc import ABC

from pyarxaas.hierarchy.level import Level


class GroupingBasedHierarchy(ABC):

    def __init__(self):
        self._levels = []
        self._level_count = 0

    @property
    def levels(self):
        return copy.deepcopy(self._levels)

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