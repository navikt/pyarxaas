import unittest

from pyaaas.privacy_models import KAnonymity
from pyaaas.models.request_builder import RequestBuilder
from tests.pyaaas import data_generator


class RequestBuilderTest(unittest.TestCase):

    def setUp(self):
        self.test_dataset = data_generator.id_name_dataset()
        self.kanon = KAnonymity(4)
        self.suplimit = 0.001
        self.expected_analyze_request = {'data': [['id', 'name'], ['0', 'Viktor'], ['1', 'Jerry']],
                                         'attributes': [{'field': 'id', 'attributeTypeModel': 'IDENTIFYING'},
                                                        {'field': 'name', 'attributeTypeModel': 'QUASIIDENTIFYING'}]}
        self.expected_anonymize_request = {'data': [['id', 'name'], ['0', 'Viktor'], ['1', 'Jerry']],
                                           'attributes': [{'field': 'id', 'attributeTypeModel': 'IDENTIFYING', 'hierarchy': None},
                                                          {'field': 'name', 'attributeTypeModel': 'QUASIIDENTIFYING', 'hierarchy': None}],
                                           'privacyModels': [{'privacyModel': 'KANONYMITY', 'params': {'k': 4}}],
                                           'suppressionLimit': 0.001}

    def test_init(self):
        RequestBuilder(self.test_dataset)

    def test_add_privacy_model(self):
        req_builder = RequestBuilder(self.test_dataset)
        req_builder.add_privacy_model(self.kanon)

    def test_add_privacy_model(self):
        req_builder = RequestBuilder(self.test_dataset)
        req_builder.add_suppression_limit(self.suplimit)

    def test_build_analyze_request(self):
        analyze_request = RequestBuilder(self.test_dataset).build_analyze_request()
        self.assertEqual(self.expected_analyze_request, analyze_request)

    def test_build_anonymize_request(self):
        anonymize_request = RequestBuilder(self.test_dataset)\
            .add_privacy_model(self.kanon)\
            .add_suppression_limit(self.suplimit)\
            .build_anonymize_request()
        self.assertEqual(self.expected_anonymize_request, anonymize_request)