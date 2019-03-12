import unittest

from pyaaas.aaas import AaaS
from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset


class AaaSTest(unittest.TestCase):


    def setUp(self):
        self.test_data = [['id', 'name'],
                         ['0', 'Viktor'],
                         ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

        self.test_dataset = Dataset(self.test_data, self.test_attribute_type_mapping)

    def test_init(self):
        AaaS('http://localhost')
        
    def test_analyze(self):
        aaas= AaaS('http://localhost')
        aaas.analyze(self.test_dataset)



