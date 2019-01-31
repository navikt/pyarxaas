import unittest
from pprint import pprint as pp
import json

from pyaaas.aaas import AaaS
from pyaaas.models.privacy_models import KAnonymity

class AaaSTest(unittest.TestCase):

    def setUp(self):
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

    def test__list_to_csv_string(self):
        result = AaaS._list_to_csv_string(self.test_hierachy_list)

    def test_run(self):
        aaas = AaaS("http://34.73.75.250:8080")
        aaas.set_data(self.test_data)
        aaas.set_attribute_type(self.test_attributes)
        aaas.set_hierarchy("zipcode", self.test_hierachy_list)
        aaas.set_model(self.test_model)
        result = aaas.anonymize()


