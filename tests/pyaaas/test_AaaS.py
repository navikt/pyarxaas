import unittest

from uplink import Body

from aaas_connector import AaaSConnector
from pyaaas import KAnonymity
from pyaaas.aaas import AaaS
from pyaaas.attribute_type import AttributeType
from pyaaas.dataset import Dataset


class MockAaasConnector(AaaSConnector):

    def anonymize_data(self, payload: Body):
        return {"data": payload["data"]}

    def risk_profile(self, payload: Body):
        return {"prosecutor_risk": 0.35}


class AaaSTest(unittest.TestCase):

    def setUp(self):
        self.test_data = [['id', 'name'],
                         ['0', 'Viktor'],
                         ['1', 'Jerry']]
        self.test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                            'name': AttributeType.QUASIIDENTIFYING}

        self.test_dataset = Dataset(self.test_data, self.test_attribute_type_mapping)

    def test_init(self):
        AaaS('http://localhost')
        
    def test_analyze(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.risk_profile(self.test_dataset))

    def test_anaonymize(self):
        aaas = AaaS('http://localhost', connector=MockAaasConnector)
        self.assertIsNotNone(aaas.anonymize(self.test_dataset, privacy_models=[KAnonymity(4)]))




