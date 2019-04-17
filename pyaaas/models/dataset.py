import copy
from collections.abc import Sequence
from collections.abc import Mapping

import pandas

from pyaaas.models.attribute_type import AttributeType


class Dataset:
    """
    Understand tabular data containing personal data.
    """

    _DEFAULT_ATTRIBUTE_TYPE = AttributeType.QUASIIDENTIFYING

    def __init__(self, data: list, attribute_types: Mapping = None):
        if attribute_types is None:
            attribute_types = self._create_default_attribute_map(data[0])

        self._data = data
        self._attributes = self._create_attributes(attribute_types)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(hash(self._data[0][0]) + self._hash_of_attributes())

    def __repr__(self) -> str:
        return f"Dataset(data={self._data}, attributes={self._attributes})"

    def describe(self):
        indent = 2
        print("data:")
        print(self._describe_data_headers(indent))
        print("rows:")
        print(self._describe_data_rows(indent))
        print("attributes:")
        print(self._describe_attributes(indent))

    def _describe_data_headers(self, indent):
        string = " "*indent + "headers:\n"
        string += " " * indent*2 + str(self._data[0])
        return string

    def _describe_data_rows(self, indent):
        indent = indent*2
        max_rows_to_print = 5
        rows_to_print = min(max_rows_to_print, (len(self._data) + 1))
        max_columns_to_print = 8
        string = ""
        for row in self._data[1:rows_to_print]:
            if len(row) > max_columns_to_print:
                columns_to_print_mid = max_columns_to_print // 2
                print_row = row[:columns_to_print_mid]
                print_row.append("...")
                print_row += row[-columns_to_print_mid:]
                row = print_row
            string += " "*indent +\
                      str(row) +\
                      "\n"
        if len(self._data) > max_rows_to_print:
            string += " "*indent + str("...")
        return string

    def _describe_attributes(self, indent):
        string = ""
        for attribute in self._attributes:
            string += " "*indent + str(attribute) + "\n"
        return string

    def _hash_of_attributes(self):
        a_hash = hash(self._attributes[0])
        for attribute in self._attributes[0:]:
            a_hash = hash(a_hash + hash(attribute))
        return a_hash

    def _has_of_data(self):
        r_hash = ""
        for row in self._data:
            for cell in row:
                r_hash = hash(r_hash + hash(cell))
        return r_hash

    def _create_attributes(self, attribute_types: Mapping):
        fields = []
        for field_name, type in attribute_types.items():
            fields.append(Dataset._Attribute(field_name, type))
        return fields

    def _create_attributes_payload(self):
        attributes = []
        for field in self._attributes:
            attributes.append(field.payload)
        return attributes

    def _payload(self):
        payload = {}
        dataset_dict = self._to_dict()
        payload["data"] = dataset_dict["data"]
        payload["attributes"] = dataset_dict["attributes"]
        return payload

    def _to_dict(self):
        return {
            "data": self._data,
            "attributes": self._create_attributes_payload()
        }

    @staticmethod
    def _create_from_hierarchy_source(source):
        if isinstance(source, Sequence):
            return copy.deepcopy(source)
        if isinstance(source, pandas.DataFrame):
            return source.values.tolist()

    @classmethod
    def from_pandas(cls, dataframe: pandas.DataFrame):
        """
        Create the dataset from a pandas DataFrame

        :param dataframe: pandas Dataframe
        :return: Dataset
        """

        headers = dataframe.columns.values.tolist()
        values = dataframe.values.tolist()
        data = [headers] + values
        return Dataset(data=data, attribute_types=cls._create_default_attribute_map(headers))

    @classmethod
    def _create_default_attribute_map(cls, fields):
        attribute_type_map = {}
        for field in fields:
            attribute_type_map[field] = cls._DEFAULT_ATTRIBUTE_TYPE
        return attribute_type_map

    def set_attribute(self, attribute, attribute_type: AttributeType):
        """
        Set Attribute type for a attribute in the dataset

        :param attribute: attribute in the dataset
        :param attribute_type: AttributeType for the attribute
        :return: None
        """

        field_map = {field.name: field for field in self._attributes}
        try:
            field_map[attribute].type = attribute_type
        except KeyError:
            raise KeyError(f"attribute=({attribute}) could not be found")

    def set_attributes(self, attributes, attribute_type: AttributeType):
        """
        Set AttributeType for a collection of attributes

        :param attributes: collection of attributes in the dataset
        :param attribute_type: AttributeType for the attributes
        :return: None
        """

        for attribute in attributes:
            self.set_attribute(attribute, attribute_type)

    def set_hierarchy(self, attribute, hierarchy):
        """
        Set hierarchy for a attribute in the Dataset

        :param attribute: attribute in the Dataset
        :param hierarchy: to be applied  to the attribute
        :return: None
        """

        hierarchy = self._create_from_hierarchy_source(hierarchy)
        field_map = {field.name: field for field in self._attributes}
        try:
            field_map[attribute].hierarchy = hierarchy
        except KeyError:
            raise KeyError(f"attribute=({attribute}) could not be found")

    def set_hierarchies(self, hierarchies):
        for attribute, hierarchy in hierarchies.items():
            self.set_hierarchy(attribute, hierarchy)

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Create pandas DataFrame of the Dataset

        :return: pandas.DataFrame
        """

        return pandas.DataFrame(self._data[1:], columns=self._data[0])

    class _Attribute:
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
            return f"_Attribute(field_name={self.name}, type={self.type}, hierarchy={self.hierarchy})"

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

        @property
        def payload(self):
            return {"field": self._field_name, "attributeTypeModel": self._type.value, "hierarchy": self._hierarchy}









