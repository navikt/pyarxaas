import unittest

from models.attribute_type import AttributeType
from models.dataset import Dataset


class AttributeTest(unittest.TestCase):

    def test_name(self):
        field = Dataset._Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual("id", field.name)

    def test_type(self):
        field = Dataset._Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, field.type.value)

