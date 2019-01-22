import unittest
from python_api_consumer.ARX_object import ARXObject

class ARXObjectTest(unittest.TestCase):

    def setUp(self):
        self.test_object = ARXObject("tom url")


    def test_init__sanity_test(self):
        obj = ARXObject("tom url")


    def test_add_data__sanity_test(self):
        self.test_object.add_data("test_data")

    def test_add_config__sanity_test(self):
        self.test_object.add_config("test_config")

