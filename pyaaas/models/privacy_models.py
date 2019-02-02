from collections.abc import Mapping
from abc import ABC, abstractproperty


class PrivacyModel(ABC):
    """ ABC for ARX Privacy Models"""

    @abstractproperty
    def name(self) -> str:
        raise NotImplementedError()


class KAnonymity(Mapping, PrivacyModel):
    """ Configuration class for KAnonymity"""


    def __init__(self, k):
        self._internal_dict = {"k": k}

    def __getitem__(self, k):
        return self._internal_dict[k]

    def __len__(self) -> int:
        return len(self._internal_dict)

    def __iter__(self):
        return iter(self._internal_dict)

    @property
    def name(self) -> str:
        return "KANONYMITY"

    def __str__(self):
        k_value = self._internal_dict["k"]
        return f"KAnonymity(k={k_value})"

