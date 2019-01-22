import unittest
from python_api_consumer import api


class APITest(unittest.TestCase):

    def test_mock_api_function__sanity_test(self):
        api.mock_api_function()


