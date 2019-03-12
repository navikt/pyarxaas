import unittest

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

