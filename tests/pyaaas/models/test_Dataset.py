import unittest

import pandas

from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.dataset import Dataset
from tests.pyaaas import data_generator


class DatasetTest(unittest.TestCase):

    def setUp(self):
        self.test_data = [['id', 'name'],
                          ['0', 'Viktor'],
                          ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

    def test_init(self):
        Dataset(self.test_data, self.test_attribute_type_mapping)

    def test_equality(self):
        dataset_1 = data_generator.id_name_dataset()
        dataset_2 = data_generator.id_name_dataset()
        self.assertEqual(dataset_1, dataset_2)
        self.assertIsNot(dataset_1, dataset_2)
        dataset_2._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        self.assertNotEqual(dataset_1, dataset_2)

    def test_hash(self):
        dataset_1 = data_generator.id_name_dataset()
        dataset_2 = data_generator.id_name_dataset()
        test_set = {dataset_1, dataset_2}
        self.assertEqual(1, len(test_set))

    def test_init__without_attribute_types_param(self):
        dataset = Dataset(self.test_data)
        self.assertEqual(dataset._DEFAULT_ATTRIBUTE_TYPE.value, dataset._attributes[0].type.value)
        self.assertEqual(self.test_data[0][0], dataset._attributes[0].name)
        self.assertEqual(self.test_data[0][1], dataset._attributes[1].name)

    def test_create_from_pandas_dataframe(self):
        dataframe = pandas.DataFrame(self.test_data[1:], columns=self.test_data[0])
        dataset = Dataset.from_pandas(dataframe)
        pandas_df = dataset.to_dataframe()

        # assert column names are in top row
        self.assertEqual(dataframe.to_dict(), pandas_df.to_dict())

        # assert default AttributeType is set
        self.assertEqual(Dataset._DEFAULT_ATTRIBUTE_TYPE.value, dataset._attributes[0].type.value)

    def test_set_attribute_types_default_value(self):
        dataset = Dataset(self.test_data)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, dataset._attributes[0].type.value)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, dataset._attributes[1].type.value)

    def test_set_attribute_type_with_sequence_of_attributes(self):
        dataset = Dataset(self.test_data)
        dataset.set_attribute_type(AttributeType.IDENTIFYING, "id", "name")
        self.assertEqual(AttributeType.IDENTIFYING.value, dataset._attributes[0].type.value)
        self.assertEqual(AttributeType.IDENTIFYING.value, dataset._attributes[1].type.value)

    def test_set_attribute_type_with_single_attribute(self):
        dataset = Dataset(self.test_data)
        dataset.set_attribute_type(AttributeType.IDENTIFYING, "id")
        self.assertEqual(AttributeType.IDENTIFYING.value, dataset._attributes[0].type.value)

    def test_set_attribute_type__single_attribute(self):
        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, dataset._attributes[0].type.value)
        self.assertEqual(Dataset._DEFAULT_ATTRIBUTE_TYPE.value, dataset._attributes[1].type.value)

    def test_set_hierarchy(self):

        test_hierarchy = [["0", "*"], ["1", "*"]]

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        dataset.set_hierarchy("id", test_hierarchy)
        self.assertEqual(dataset._attributes[0].hierarchy, test_hierarchy)

    def test_set_hierarchy__not_valid_attribute_name(self):

        test_hierarchy = [["0", "*"], ["1", "*"]]

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        with self.assertRaises(KeyError):
            dataset.set_hierarchy("fail", test_hierarchy)
        self.assertIsNone(dataset._attributes[0].hierarchy)

    def test_set_hierarchy__not_valid_attribute_type(self):

        test_hierarchy = [["0", "*"], ["1", "*"]]

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.INSENSITIVE)
        with self.assertRaises(ValueError):
            dataset.set_hierarchy("id", test_hierarchy)
        self.assertIsNone(dataset._attributes[0].hierarchy)
        self.assertIsNot(test_hierarchy, dataset._attributes[0].hierarchy)

    def test_set_hierarchies(self):

        test_hierarchy_id = [["0", "*"], ["1", "*"]]
        test_hierarchy_name = [["Viktor", "*"], ["Jerry", "*"]]

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        dataset._set_attribute_type("name", AttributeType.QUASIIDENTIFYING)
        dataset.set_hierarchies({"id": test_hierarchy_id, "name": test_hierarchy_name})
        self.assertEqual(dataset._attributes[0].hierarchy, test_hierarchy_id)
        self.assertEqual(dataset._attributes[1].hierarchy, test_hierarchy_name)

    def test_set_hierarchy_with_pandas(self):

        test_hierarchy = [["0", "*"], ["1", "*"]]
        hierarchy_df = pandas.DataFrame(test_hierarchy)

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        dataset.set_hierarchy("id", hierarchy_df)
        self.assertEqual(dataset._attributes[0].hierarchy, test_hierarchy)

    def test__payload(self):
        dataset = Dataset(self.test_data)
        payload = dataset._payload()
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, payload["attributes"][0]["attributeTypeModel"])
        self.assertEqual(None, payload["attributes"][0]["hierarchy"])

    def test__payload__with_hierarchies(self):

        test_hierarchy_id = [["0", "*"], ["1", "*"]]
        test_hierarchy_name = [["Viktor", "NAME"], ["Jerry", "NAME"]]

        dataset = Dataset(self.test_data)
        dataset._set_attribute_type("id", AttributeType.QUASIIDENTIFYING)
        dataset._set_attribute_type("name", AttributeType.QUASIIDENTIFYING)
        dataset.set_hierarchies({"id": test_hierarchy_id, "name": test_hierarchy_name})
        payload = dataset._payload()
        self.assertEqual(test_hierarchy_id, payload["attributes"][0]["hierarchy"])
        self.assertEqual(test_hierarchy_name, payload["attributes"][1]["hierarchy"])

    def test_to_dataframe(self):
        dataset = Dataset(self.test_data, self.test_attribute_type_mapping)
        df = dataset.to_dataframe()
        self.assertIsInstance(df, pandas.DataFrame)

    def test_from_dict(self):
        data = {"id": [1, 2], "name": ["Monsen", "Mikkel"]}
        expected_df = pandas.DataFrame.from_dict(data)
        dataset = Dataset.from_dict(data)
        self.assertIsNotNone(dataset)
        self.assertIsInstance(dataset, Dataset)
        self.assertEqual(expected_df.to_dict(), dataset.to_dataframe().to_dict())


