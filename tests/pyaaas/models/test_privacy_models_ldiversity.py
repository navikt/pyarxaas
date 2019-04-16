from pyaaas.privacy_models import LDiversityDistinct, LDiversityGrassbergerEntropy, LDiversityShannonEntropy, LDiversityRecursive
import unittest


class PrivacyModelsLDiversityTest(unittest.TestCase):

    def test_privacyModelIterator(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(list(iter(self.privacymodel))[1], "column_name", "Iterator does not create correct list of values")


    def test_lenght(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(len(self.privacymodel), 2)


    def test_message(self):
        self.privacymodel = LDiversityDistinct(l=3, column_name="column")
        self.assertEqual(str(self.privacymodel), "LDiversityDistinct(l=3, column_name=column)")

    def test_set_data_distinct(self):
        self.distict = LDiversityDistinct(l=3, column_name="sensitive_column_name")
        self.assertEqual(self.distict._anonymity_name, "LDIVERSITY_DISTINCT", "Recursive model name not correct")

    def test_set_data_grassberger(self):
        self.grassberger = LDiversityGrassbergerEntropy(l=3, column_name="sensitive_column_name")
        self.assertEqual(self.grassberger._anonymity_name, "LDIVERSITY_GRASSBERGERENTROPY", "Grassberger model name not correct")

    def test_set_data_shannonentropy(self):
        self.shannon_entropy = LDiversityShannonEntropy(l=3, column_name="sensitive_column_name")
        self.assertEqual(self.shannon_entropy.get("l"), 3, "l_value does not equals 3")
        self.assertNotEqual(self.shannon_entropy.get("l"), 1, "l_Value does equals 1")
        self.assertEqual(self.shannon_entropy.get("column_name"), "sensitive_column_name", "Columnname is set correctly")
        self.assertNotEqual(self.shannon_entropy.get("column_name"), "unsensitive_column_name", "Columnname is not set incorrectly")
        self.assertEqual(self.shannon_entropy._anonymity_name, "LDIVERSITY_SHANNONENTROPY", "Anonymity name not set correctly")

    def test_set_data_recursive(self):
        self.recursive = LDiversityRecursive(l=3, c=1, column_name="sensitive_column_name")
        self.assertEqual(self.recursive._anonymity_name, "LDIVERSITY_RECURSIVE", "Recursive model name not correct")
