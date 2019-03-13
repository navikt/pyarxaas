import unittest

import pandas

from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset


class DatasetTest(unittest.TestCase):

    def setUp(self):
        self.test_data = [['id', 'name'],
                         ['0', 'Viktor'],
                         ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

    def test_init(self):
        Dataset(self.test_data, self.test_attribute_type_mapping)

    def test_init__without_attribute_types_param(self):
        dataset = Dataset(self.test_data)
        self.assertEqual(dataset.DEFAULT_ATTRIBUTE_TYPE.value, dataset._fields[0].type.value)
        self.assertEqual(self.test_data[0][0], dataset._fields[0].name)
        self.assertEqual(self.test_data[0][1], dataset._fields[1].name)

    def test_create_from_pandas_dataframe(self):
        dataframe = pandas.DataFrame(self.test_data[1:], columns=self.test_data[0])
        dataset = Dataset.from_pandas(dataframe)

        # assert column names are in top row
        self.assertEqual("id", dataset._data[0][0])
        self.assertEqual("name", dataset._data[0][1])

        # assert default AttributeType is set
        self.assertEqual(Dataset.DEFAULT_ATTRIBUTE_TYPE.value, dataset._fields[0].type.value)

    def test_set_attribute_type(self):
        dataset = Dataset(self.test_data)
        dataset.set_attribute(["id", "name"], AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, dataset._fields[0].type.value)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, dataset._fields[1].type.value)

