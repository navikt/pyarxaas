import unittest

import pandas

from pyaaas.models.dataset.data import Data
from pyaaas.models.attribute_type import AttributeType
from pyaaas.models.dataset import Dataset
from tests.pyaaas import data_generator


class DataTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        Data(headers=["id", "name"], rows=[["1", "Max"]])

    def test_payload(self):
        data = Data(headers=["id", "name"], rows=[["1", "Max"]])
        self.assertEqual([["id", "name"], ["1", "Max"]], data.payload)