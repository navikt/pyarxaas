from pyaaas.models.privacy_models import LDiversityDistinct
import unittest

class PrivacyModelsTest(unittest.TestCase):

    def test_privacyModelIterator(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(list(iter(self.privacymodel))[1], "column_name", "Iterator does not create correct list of values")


    def test_lenght(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(len(self.privacymodel), 2)


    def test_message(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(str(self.privacymodel), "LDiversityDistinct(l=3, column_name=column)")

