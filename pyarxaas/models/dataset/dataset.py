import copy
from collections.abc import Sequence
from collections.abc import Mapping

import pandas

from pyarxaas.models.dataset.data import Data
from pyarxaas.models.dataset.attribute import Attribute
from pyarxaas.models.attribute_type import AttributeType


class Dataset:
    """
    Understand tabular data containing personal data.
    """

    _DEFAULT_ATTRIBUTE_TYPE = AttributeType.QUASIIDENTIFYING

    def __init__(self, data: list, attribute_types: Mapping = None):
        if attribute_types is None:
            attribute_types = self._create_default_attribute_map(data[0])

        self._data = Data(data[0], data[1:])
        self._attributes = self._create_attributes(attribute_types)

    def _set_attribute_type(self, attribute, attribute_type: AttributeType):
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

    def set_attribute_type(self, attribute_type: AttributeType, *attributes):
        """
        Set AttributeType for a collection of attributes

        :param attributes: collection of attributes in the dataset
        :param attribute_type: AttributeType for the attributes
        :return: None
        """
        for attribute in attributes:
            self._set_attribute_type(attribute, attribute_type)

    def _create_attributes(self, attribute_types: Mapping):
        fields = []
        for field_name, type in attribute_types.items():
            fields.append(Attribute(field_name, type))
        return fields

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

        return self._data.dataframe

    def describe(self):
        """
        Prints a description of the Dataset to stdout

        :return: None
        """

        indent = 2
        self._data.describe(indent)
        print("attributes:")
        print(self._describe_attributes(indent))

    def _describe_attributes(self, indent):
        string = ""
        for attribute in self._attributes:
            string += " "*indent + str(attribute) + "\n"
        return string

    def _payload(self):
        payload = {}
        dataset_dict = self._to_dict()
        payload["data"] = dataset_dict["data"]
        payload["attributes"] = dataset_dict["attributes"]
        return payload

    def _to_dict(self):
        return {
            "data": self._data.payload,
            "attributes": self._create_attributes_payload()
        }

    def _create_attributes_payload(self):
        attributes = []
        for field in self._attributes:
            attributes.append(field.payload)
        return attributes

    @classmethod
    def from_pandas(cls, dataframe: pandas.DataFrame):
        """
        Create a Dataset from a pandas DataFrame

        :param dataframe: pandas Dataframe
        :return: Dataset
        """

        headers = dataframe.columns.values.tolist()
        values = dataframe.values.tolist()
        data = [headers] + values
        return Dataset(data=data, attribute_types=cls._create_default_attribute_map(headers))

    @classmethod
    def from_dict(cls, dictionary):
        """
        Create Dataset from a python dictionary

        :param dictionary: Mapping object to create Dataset from
        :return: Dataset
        """

        df = pandas.DataFrame.from_dict(dictionary)
        return cls.from_pandas(df)

    @classmethod
    def _create_default_attribute_map(cls, fields):
        attribute_type_map = {}
        for field in fields:
            attribute_type_map[field] = cls._DEFAULT_ATTRIBUTE_TYPE
        return attribute_type_map

    @staticmethod
    def _create_from_hierarchy_source(source):
        if isinstance(source, Sequence):
            return copy.deepcopy(source)
        if isinstance(source, pandas.DataFrame):
            return source.values.tolist()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(hash(self._data) + self._hash_of_attributes())

    def _hash_of_attributes(self):
        a_hash = hash(self._attributes[0])
        for attribute in self._attributes[0:]:
            a_hash = hash(a_hash + hash(attribute))
        return a_hash

    def __repr__(self) -> str:
        return f"Dataset(data={self._data}, attributes={self._attributes})"













