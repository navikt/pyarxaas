from collections.abc import Mapping
from abc import ABC, abstractproperty


class PrivacyModel(ABC, Mapping):
    """ ABC for ARX Privacy Models"""
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


class KAnonymity(PrivacyModel):
    """ Configuration class for KAnonymity"""

    def __init__(self, k):
        self._internal_dict = {"k": k}
        self._anonymity_name = "KANONYMITY"
        self._print_message = f"KAnonymity(k={k})"


class LDiversityDistinct(PrivacyModel):
    """ Configuration class for LDiversity"""

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_DISTINCT"
        self._print_message = f"LDiversityDistinct(l={l}, column_name={column_name})"


class LDiversityShannonEntropy(PrivacyModel):
    """ Configuration class for LDiversity"""

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_SHANNONENTROPY"
        self._print_message = f"LDiversityShannonEntropy(l={l}, column_name={column_name})"


class LDiversityGrassbergerEntropy(PrivacyModel):
    """ Configuration class for LDiversity"""

    def __init__(self, l, column_name):
        self._internal_dict = {"l": l, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_GRASSBERGERENTROPY"
        self._print_message = f"LDiversityGrassbergerEntropy(l={l}, column_name={column_name})"


class LDiversityRecursive(PrivacyModel):
    """ Configuration class for LDiversity"""

    def __init__(self, l, c, column_name):
        self._internal_dict = {"l": l, "c": c, "column_name": column_name}
        self._anonymity_name = "LDIVERSITY_RECURSIVE"
        self._print_message = f"LDiversityRecursive(l={l}, c={c}, column_name={column_name})"
