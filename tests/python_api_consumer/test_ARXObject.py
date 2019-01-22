import unittest
from python_api_consumer.ARX_object import ARXObject

class ARXObjectTest(unittest.TestCase):

    def test_init__sanity_test(self):
        obj = ARXObject("tom url")
