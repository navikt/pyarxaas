import uuid


class Level:
    """
    Represent a given level in a hierarchy builder
    """

    def __init__(self, level):
        self._level = level
        self._groups = {}

    def add_group(self, grouping, label=None) -> "Level":
        self._groups[Group(grouping, label)] = None
        return self

    def payload(self):
        return {"level": self._level,
                "groups": [group.payload() for group in self._groups.keys()]}

    def __repr__(self):
        return f"Level(level={self._level}, groups={self._groups})"

    def __str__(self):
        return f"level={self._level}, groups={self._groups}"


class Group:
    """
    Represents a group in a hierarchy Level
    """

    def __init__(self, grouping, label):
        self._grouping = grouping
        self._label = label

    def payload(self):
        return {"grouping": self._grouping,
                "label": self._label}

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        # Groups are only equal if labels are present and the same
        label = self._label
        if label is None:
            label = uuid.uuid1()
        return hash(self._grouping) + hash(label)

    def __repr__(self):
        return f"Group(grouping={self._grouping}, label={self._label})"

    def __str__(self):
        return f"grouping={self._grouping}, label={self._label}"





