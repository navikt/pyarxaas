from collections.abc import Mapping
class Dataset:
    """
    Understand tabular data containing personal data.
    """
    def __init__(self, data: list, attribute_types: Mapping):
        self._data = data
        self._fields = self._create_fields(attribute_types)

    def _create_fields(self, attribute_types: Mapping):
        fields = []
        for field_name, type in attribute_types.items():
            fields.append(Field(field_name, type))
        return fields

    def to_dict(self):
        return {
            "data": self._data,
            "attribute_types": self._create_attribute_map()
        }

    def _create_attribute_map(self):
        attribute_map = {}
        for field in self._fields:
            attribute_map[field._field_name] = field._type
        return attribute_map




class Field:
    """
    Understands Dataset field
    """
    def __init__(self, field_name, type):
        self._field_name = field_name
        self._type = type
