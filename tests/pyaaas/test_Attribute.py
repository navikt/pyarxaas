import unittest

from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset


class FieldTest(unittest.TestCase):

    def test_name(self):
        field = Dataset._Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual("id", field.name)

    def test_type(self):
        field = Dataset._Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, field.type.value)

