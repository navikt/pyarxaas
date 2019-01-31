import unittest
from pprint import pprint as pp
import json
import pandas as pd

from pyaaas.aaas import AaaS
from pyaaas.models.privacy_models import KAnonymity
from pyaaas.models.anonymize_result import AnonymizeResult


class MockRequestResult:
    """ Mock class for requests result object"""

    @property
    def text(self):
        return '{"test": "test"}'


class AaaSTest(unittest.TestCase):

    def setUp(self):

        self.test_data_dict = {'age': {0: 34,
  1: 35,
  2: 36,
  3: 37,
  4: 38,
  5: 39,
  6: 40,
  7: 41,
  8: 42,
  9: 43,
  10: 44},
 ' gender': {0: ' male',
  1: ' female',
  2: ' male',
  3: ' female',
  4: ' male',
  5: ' female',
  6: ' male',
  7: ' female',
  8: ' male',
  9: ' female',
  10: ' male'},
 ' zipcode': {0: 81667,
  1: 81668,
  2: 81669,
  3: 81670,
  4: 81671,
  5: 81672,
  6: 81673,
  7: 81674,
  8: 81675,
  9: 81676,
  10: 81677}}

        self.test_df = pd.DataFrame(self.test_data_dict)

        self.test_hierachy_list = [['81667','8166*', '816**', '81***', '8****', '*****'],
    ['81668', '8166*', '816**', '81***', '8****', '*****'],
    ['81669', '8166*', '816**', '81***', '8****', '*****'],
    ['81670', '8167*', '816**', '81***', '8****', '*****'],
    ['81671', '8167*', '816**', '81***', '8****', '*****'],
    ['81672', '8167*', '816**', '81***', '8****', '*****'],
    ['81673', '8167*', '816**', '81***', '8****', '*****'],
    ['81674', '8167*', '816**', '81***', '8****', '*****'],
    ['81675', '8167*', '816**', '81***', '8****', '*****'],
    ['81676', '8167*', '816**', '81***', '8****', '*****'],
    ['81677', '8167*', '816**', '81***', '8****', '*****']]

        self.test_model = KAnonymity(k=4)
        self.test_attributes = {"age":"IDENTIFYING",
                           "gender":"INSENSITIVE",
                           "zipcode":"INSENSITIVE"}
        self.test_data = "age, gender, zipcode\n34, male, 81667\n35, female, 81668\n36, male, 81669\n37, female, 81670\n38, male, 81671\n39, female, 81672\n40, male, 81673\n41, female, 81674\n42, male, 81675\n43, female, 81676\n44, male, 81677"

        aaas = AaaS("http://34.73.75.250:8080")
        aaas.set_data(self.test_data)
        aaas.set_attribute_type(self.test_attributes)
        aaas.set_hierarchy("zipcode", self.test_hierachy_list)
        aaas.set_model(self.test_model)
        self.test_aaas = aaas

    def mock_anonymize_data(self, *args, **kwargs):
        return MockRequestResult()

    def test_run(self):
        aaas = AaaS("test_url")
        aaas._conn.anonymize_data = self.mock_anonymize_data
        aaas.set_data(self.test_data)
        aaas.set_attribute_type(self.test_attributes)
        aaas.set_hierarchy("zipcode", self.test_hierachy_list)
        aaas.set_model(self.test_model)
        result = aaas.anonymize()
        self.assertIsInstance(result, AnonymizeResult)

