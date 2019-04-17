import unittest

from models.dataset.attribute import Attribute
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.dataset import Dataset


class AttributeTest(unittest.TestCase):

    def test_name(self):
        field = Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual("id", field.name)

    def test_type(self):
        field = Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, field.type.value)

