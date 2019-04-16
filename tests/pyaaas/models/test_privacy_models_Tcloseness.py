from pyaaas.privacy_models import TClosenessEqualDistance, TClosenessOrderedDistance
import unittest


class PrivacyModelsTclosenessTest(unittest.TestCase):

    def test_privacyModelIterator(self):
        self.privacymodel = TClosenessEqualDistance(t=3, column_name="column")
        self.assertEqual(list(iter(self.privacymodel))[1], "column_name", "Iterator does not create correct list of values")

    def test_lenght(self):
        self.privacymodel = TClosenessEqualDistance(t=3, column_name="column")
        self.assertEqual(len(self.privacymodel), 2)

    def test_message(self):
        self.privacymodel = TClosenessEqualDistance(t=3, column_name="column")
        self.assertEqual(str(self.privacymodel), "TClosenessEqualDistance(t=3, column_name=column)")

    def test_set_data_EqualDistance(self):
        self.distict = TClosenessEqualDistance(t=3, column_name ="sensitive_column_name")
        self.assertEqual(self.distict._anonymity_name, "TCLOSENESS_EQUAL_DISTANCE", "Recursive model name not correct")

    def test_set_data_TClosenessOrderedDistance(self):
        self.distict = TClosenessOrderedDistance(t=3, column_name="sensitive_column_name")
        self.assertEqual(self.distict._anonymity_name, "TCLOSENESS_ORDERED_DISTANCE", "Recursive model name not correct")