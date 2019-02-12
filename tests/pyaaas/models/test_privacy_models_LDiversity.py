from pyaaas.models.privacy_models import LDiversityShannonEntropy
import unittest

class PrivacyModelsLDiversityTest(unittest.TestCase):

    def test_set_data(self):
        self.shannon_entropy = LDiversityShannonEntropy(l=3, column_name="sensitive_column_name")

        self.assertEqual(self.shannon_entropy.get("l"), 3, "l_value does not equals 3")
        self.assertNotEqual(self.shannon_entropy.get("l"), 1, "l_Value does equals 1")

        self.assertEqual(self.shannon_entropy.get("column_name"), "sensitive_column_name", "Columnname is set correctly")
        self.assertNotEqual(self.shannon_entropy.get("column_name"), "unsensitive_column_name", "Columnname is not set incorrectly")

        self.assertEqual(self.shannon_entropy._anonymity_name, "LDIVERSITY_SHANNONENTROPY", "Anonymity name not set correctly")