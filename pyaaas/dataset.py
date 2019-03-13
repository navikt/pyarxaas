from collections.abc import Sequence

import pandas
from collections.abc import Mapping

from attribute_type import AttributeType


class Dataset:
    """
    Understand tabular data containing personal data.
    """
    DEFAULT_ATTRIBUTE_TYPE = AttributeType.INSENSITIVE

    def __init__(self, data: list, attribute_types: Mapping = None):
        if attribute_types is None:
            attribute_types = self._create_default_attribute_map(data[0])

        self._data = data
        self._fields = self._create_attributes(attribute_types)

    def _create_attributes(self, attribute_types: Mapping):
        fields = []
        for field_name, type in attribute_types.items():
            fields.append(Dataset.Attribute(field_name, type))
        return fields

    def _create_attribute_map(self):
        attribute_map = {}
        for field in self._fields:
            attribute_map[field.name] = str(field.type)
        return attribute_map

    def _to_payload(self):
        payload = {}
        dataset_dict = self._to_dict()
        payload["data"] = dataset_dict["data"]
        payload["attributeTypes"] = dataset_dict["attribute_types"]
        return payload

    def _to_dict(self):
        return {
            "data": self._data,
            "attribute_types": self._create_attribute_map()
        }

    @classmethod
    def from_pandas(cls, dataframe: pandas.DataFrame):
        headers = dataframe.columns.values.tolist()
        values = dataframe.values.tolist()
        data = [headers] + values
        return Dataset(data=data, attribute_types=cls._create_default_attribute_map(headers))

    @classmethod
    def _create_default_attribute_map(cls, fields):
        attribute_type_map = {}
        for field in fields:
            attribute_type_map[field] = cls.DEFAULT_ATTRIBUTE_TYPE
        return attribute_type_map

    def set_attribute(self, attribute, attribute_type: AttributeType):
        field_map = {field.name: field for field in self._fields}
        try:
            field_map[attribute].type = attribute_type
        except KeyError:
            raise KeyError(f"attribute=({attribute}) could not be found")

    def set_attributes(self, attributes, attribute_type: AttributeType):
        for attribute in attributes:
            self.set_attribute(attribute, attribute_type)

    def set_hierarchy(self, attribute, hierarchy):
        field_map = {field.name: field for field in self._fields}
        try:
            field_map[attribute].hierarchy = hierarchy
        except KeyError:
            raise KeyError(f"attribute=({attribute}) could not be found")

    def set_hierarchies(self, hierarchies):
        for attribute, hierarchy in hierarchies.items():
            self.set_hierarchy(attribute, hierarchy)

    class Attribute:
        """
        Understands Dataset field
        """

        def __init__(self, field_name, type):
            self._field_name = field_name
            self._type = type
            self._hierarchy = None

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
                raise ValueError(f"{self.__class__}(name={self.name}, type={self.type}) has to be of type {AttributeType.QUASIIDENTIFYING}")
            self._hierarchy = hierarchy

        def _is_hierarchy_settable(self):
            return AttributeType.QUASIIDENTIFYING.value == self.type.value







