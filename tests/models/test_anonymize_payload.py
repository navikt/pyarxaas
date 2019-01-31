import unittest
from pprint import pprint as pp

from pyaaas.models.anonymize_payload import AnonymizePayload, PayloadJSONConverter
from pyaaas.models.privacy_models import KAnonymity
import json

class AnonymizationPayloadTest(unittest.TestCase):

    def setUp(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        self.test_payload = anon_payload

    def test_init_run(self):
        ap = AnonymizePayload()


    def test_convert_to_json(self):
        anon_payload = AnonymizePayload()
        kanon = KAnonymity(k=4)
        anon_payload.metadata["models"][kanon.name] = kanon
        result_dict = {**anon_payload}
        models = {}
        for key, value in anon_payload.metadata["models"].items():
            model_dict = {**value}
            models[key] = model_dict
        result_dict["metadata"]["models"] = models
        print(str(result_dict))


    def test__convert_payload_to_backed_schema_contains_correct_schema(self):
        result = json.dumps(self.test_payload, cls=PayloadJSONConverter)


