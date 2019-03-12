import unittest

import pandas

from pyaaas.models.anonymize_payload import AnonymizePayload
from pyaaas.models.privacy_models import KAnonymity


class KAnonymizationPayloadTest(unittest.TestCase):

    def setUp(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        self.test_payload = anon_payload
        self.test_dataframe = pandas.DataFrame.from_dict({"id": [1,2,3],
                                                          "name": ["Mike", "Sarah", "Morten"],
                                                          "age": [10, 23, 43]} )

    def test_init_run(self):
        AnonymizePayload()

    def test_set_data__add_dataframe(self):
        self.test_payload.data = self.test_dataframe
        self.assertIsInstance(self.test_payload.data, list)


class LAnonymizationPayloadTest(unittest.TestCase):

    def setUp(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        self.test_payload = anon_payload
        self.test_dataframe = pandas.DataFrame.from_dict({"id": [1,2,3],
                                                          "name": ["Mike", "Sarah", "Morten"],
                                                          "age": [10, 23, 43]} )

    def test_init_run(self):
        AnonymizePayload()

    def test_set_data__add_dataframe(self):
        self.test_payload.data = self.test_dataframe
        self.assertIsInstance(self.test_payload.data, list)




