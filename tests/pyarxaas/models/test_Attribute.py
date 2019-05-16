import unittest

from pyarxaas.models.dataset.attribute import Attribute
from pyarxaas.models.attribute_type import AttributeType


class AttributeTest(unittest.TestCase):

    def test_name(self):
        field = Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual("id", field.name)

    def test_type(self):
        field = Attribute("id", AttributeType.QUASIIDENTIFYING)
        self.assertEqual(AttributeType.QUASIIDENTIFYING.value, field.type.value)

