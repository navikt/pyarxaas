import unittest

import pandas

from pyarxaas.models.dataset.data import Data
from pyarxaas.models.attribute_type import AttributeType
from pyarxaas.models.dataset import Dataset
from tests.pyarxaas import data_generator


class DataTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        Data(headers=["id", "name"], rows=[["1", "Max"]])

    def test_payload(self):
        data = Data(headers=["id", "name"], rows=[["1", "Max"]])
        self.assertEqual([["id", "name"], ["1", "Max"]], data.payload)