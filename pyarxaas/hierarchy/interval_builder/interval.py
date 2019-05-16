
class Interval:

    def __init__(self, from_, to, label: str = None):
        if from_ > to:
            raise AttributeError(f"from={from_} cannot be bigger than to={to}")
        self._from = from_
        self._to = to
        self._label = label

    def payload(self):
        return {"from": self._from,
                "to": self._to,
                "label": self._label}

    def is_decimal(self):
        if isinstance(self._from, float) or isinstance(self._to, float):
            return True
        return False

    def __repr__(self):
        return f"Interval(from={self._from}, to={self._to}, label={self._label})"

    def __str__(self):
        return f"from={self._from}, to={self._to}, label={self._label}"

    def __eq__(self, other):
        if isinstance(other, Interval):
            return hash(other) == hash(self)
        return False

    def __hash__(self):
        return hash(self._from) + hash(self._to) + hash(self._label)
