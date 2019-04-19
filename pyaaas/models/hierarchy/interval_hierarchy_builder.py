class Group:

    def __init__(self, grouping, label):
        self._grouping = grouping
        self._label = label

    def payload(self):
        return {"grouping": self._grouping,
                "label": self._label}


class Level:

    def __init__(self, level):
        self._level = level
        self._groups = []

    def add_group(self, grouping, label=None):
        self._groups.append(Group(grouping, label))

    def payload(self):
        return {"level": self._level,
                "groups": [group.payload() for group in self._groups]}


class Interval:

    def __init__(self, from_, to, label):
        if from_ > to:
            raise AttributeError(f"from={from_} cannot be bigger than to={to}")
        self._from = from_
        self._to = to
        self._label = label

    def payload(self):
        return {"from": self._from,
                "to": self._to,
                "label": self._label}


class IntervalHierarchyGenerator:

    def __init__(self):
        self._levels = []
        self._intervals = []
        self._level_count = 0
        self._column = None

    def add_interval(self, from_, to, label: str=None):
        self._intervals.append(Interval(from_, to, label))

    def level(self, level):
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
                "levels": [level.payload() for level in self._levels]
            }
        }
