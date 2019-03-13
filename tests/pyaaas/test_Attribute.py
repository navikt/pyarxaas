import unittest

from attribute_type import AttributeType
from dataset import Dataset


class FieldTest(unittest.TestCase):

    def test_name(self):
        field = Dataset.Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual("id", field.name)

    def test_type(self):
        field = Dataset.Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, field.type.value)

