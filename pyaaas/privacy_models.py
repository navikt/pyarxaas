from collections.abc import Mapping
from abc import ABC


class PrivacyModel(ABC, Mapping):
    """
    Documentation of the privacy models implemented in the ARXaaS service and the definition of the parameters
    each privacy model takes.
    """
    def __init__(self):
        self._internal_dict = {}

    def __getitem__(self, item):
        return self._internal_dict[item]

    def __len__(self) -> int:
        return len(self._internal_dict)

    def __iter__(self):
        return iter(self._internal_dict)

    @property
    def name(self) -> str:
        return self._anonymity_name

    def __str__(self):
        return self._print_message

    def _payload(self):
        return {"privacyModel": self.name, "params": self._internal_dict}


class KAnonymity(PrivacyModel):
    """
    Configuration class for K-Anonymity

    :param k: Value of K  to anonymize the dataset. K must have a value of 2 or higher to take effect.

    """

    def __init__(self, k):
        self._internal_dict = {"k": k}
        self._anonymity_name = "KANONYMITY"
        self._print_message = f"KAnonymity(k={k})"


class LDiversityDistinct(PrivacyModel):
    """
    Configuration class for Distinct L-Diversity

    :param l: Value of L to anonymize the dataset based on a column or dataset field that has a sensitive attribute. L must have a value of 2 or higher to take effect.
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_DISTINCT"
        self._print_message = f"LDiversityDistinct(l={l}, column_name={column_name})"


class LDiversityShannonEntropy(PrivacyModel):
    """
    Configuration class for Shannon Entropy L-Diversity

    :param l: Value of L to anonymize the dataset based on a column or dataset field that has a sensitive attribute. L must have a value of 2 or higher to take effect.
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_SHANNONENTROPY"
        self._print_message = f"LDiversityShannonEntropy(l={l}, column_name={column_name})"


class LDiversityGrassbergerEntropy(PrivacyModel):
    """ Configuration class for Grassberger Entropy L-Diversity

    :param l: Value of L to anonymize the dataset based on a column or dataset field that has a sensitive attribute. L must have a value of 2 or higher to take effect.
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_GRASSBERGERENTROPY"
        self._print_message = f"LDiversityGrassbergerEntropy(l={l}, column_name={column_name})"


class LDiversityRecursive(PrivacyModel):
    """ Configuration class for Recursive L-Diversity

    :param l: Value of L to anonymize the dataset based on a column or dataset field that has a sensitive attribute. L must have a value of 2 or higher to take effect.
    :param c: Value of C to anonymize the dataset based on a column or dataset field that has a sensitive attribute. c must have a value of  0.00001 or higher to take effect.
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, l, c, column_name):
        self._internal_dict = {"l": l, "c": c, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_RECURSIVE"
        self._print_message = f"LDiversityRecursive(l={l}, c={c}, column_name={column_name})"

class TClosenessOrderedDistance(PrivacyModel):
    """
    Configuration class for Ordered Distance T-Closeness

    :param t: Value of T to anonymize the dataset based on a column or dataset field that has a sensitive attribute. T must have a value between 0.000001 to 1.0
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, t, column_name):
        self._internal_dict = {"t": t, "column_name": column_name}
        self._anonymity_name = "TCLOSENESS_ORDERED_DISTANCE"
        self._print_message = f"TClosenessOrderedDistance(t={t}, column_name={column_name})"

class TClosenessEqualDistance(PrivacyModel):
    """
    Configuration class for Equal Distance T-Closeness

    :param t: Value of T to anonymize the dataset based on a column or dataset field that has a sensitive attribute. T must have a value between 0.000001 to 1.0
    :param column_name: Column or dataset field that has a sensitive attribute type.
    """

    def __init__(self, t, column_name):
        self._internal_dict = {"t": t, "column_name": column_name}
        self._anonymity_name = "TCLOSENESS_EQUAL_DISTANCE"
        self._print_message = f"TClosenessEqualDistance(t={t}, column_name={column_name})"