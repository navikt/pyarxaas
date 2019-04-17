from collections import Sequence

from pyaaas.models.attribute_type import AttributeType


class Attribute:
    """
    Understands Dataset field
    """

    def __init__(self, field_name, type):
        self._field_name = field_name
        self._type = type
        self._hierarchy = None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(hash(self._field_name) + hash(self._hierarchy) + hash(self._type))

    def __str__(self) -> str:
        return f"field_name={self.name}, type={self.type.name}, hierarchy={self.hierarchy}"

    def __repr__(self):
        return f"Attribute(field_name={self.name}, type={self.type}, hierarchy={self.hierarchy})"

    @property
    def name(self):
        return self._field_name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, attribute_type):
        attribute_type = AttributeType(attribute_type.value)
        self._type = attribute_type

    @property
    def hierarchy(self):
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy):
        if not isinstance(hierarchy, Sequence):
            raise ValueError(f"hierarchy has to be of type {Sequence}")
        if not self._is_hierarchy_settable():
            raise ValueError(
                f"{self.__class__}(name={self.name}, type={self.type}) has to be of type {AttributeType.QUASIIDENTIFYING}")
        self._hierarchy = hierarchy

    def _is_hierarchy_settable(self):
        return AttributeType.QUASIIDENTIFYING.value == self.type.value

    @property
    def payload(self):
        return {"field": self._field_name, "attributeTypeModel": self._type.value, "hierarchy": self._hierarchy}