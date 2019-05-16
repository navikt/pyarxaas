import unittest

import pandas

from pyarxaas import converters
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct, LDiversityRecursive


class ConvertersTest(unittest.TestCase):

    def setUp(self):
        self.test_hierarchy_mapping = {'zipcode': [['81667', '8166*', '816**', '81***', '8****', '*****'],
                                            ['81668', '8166*', '816**', '81***', '8****', '*****'],
                                            ['81669', '8166*', '816**', '81***', '8****', '*****'],
                                            ['81670', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81671', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81672', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81673', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81674', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81675', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81676', '8167*', '816**', '81***', '8****', '*****'],
                                            ['81677', '8167*', '816**', '81***', '8****', '*****']]}

        self.test_privacy_models_sequence = [KAnonymity(k=4), LDiversityDistinct(2, "test_column")]
        self.test_attribute_types_mapping = {"id": "INDENTIFING",
                                             "name": "QUASIIDENTIFING"}

    def test_create_transform_models_dataframe__run(self):
        dataframe = converters.create_transform_models_dataframe(self.test_hierarchy_mapping)
        self.assertIsNotNone(dataframe)
        self.assertIsInstance(dataframe, pandas.DataFrame)


    def test_create_privacy_models_dataframe__run(self):
        dataframe = converters.create_privacy_models_dataframe(self.test_privacy_models_sequence)
        self.assertIsNotNone(dataframe)
        self.assertIsInstance(dataframe, pandas.DataFrame)

    def test_create_attribute_types_dataframe__run(self):
        dataframe = converters.create_attribute_types_dataframe(self.test_attribute_types_mapping)
        self.assertIsNotNone(dataframe)
        self.assertIsInstance(dataframe, pandas.DataFrame)
