import unittest
from python_api_consumer.aaas import AaaS

class AaaSTest(unittest.TestCase):

    def setUp(self):
        self.test_object = AaaS("tom url")


    def test_init__sanity_test(self):
        obj = AaaS("tom url")


    def test_add_data__sanity_test(self):
        self.test_object.add_data("test_data")

    def test_add_config__sanity_test(self):
        self.test_object.add_config("test_config")

