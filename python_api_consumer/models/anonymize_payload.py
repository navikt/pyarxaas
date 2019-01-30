from collections.abc import MutableMapping
from typing import Iterator, _T_co, _KT, _VT_co, _VT


class AnonymizePayload(MutableMapping):
    """
    Anonymization data and meta data container
    """

    def __init__(self, data: str, meta_data: MutableMapping):
        self._internal_dict = {"data": data, "metadata": meta_data}

    def __setitem__(self, k: _KT, v: _VT) -> None:
        self._internal_dict[k] = v

    def __delitem__(self, v: _KT) -> None:
        del self._internal_dict[v]

    def __getitem__(self, k: _KT) -> _VT_co:
        return self._internal_dict[k]

    def __len__(self) -> int:
        return  len(self._internal_dict)

    def __iter__(self) -> Iterator[_T_co]:
        return iter(self._internal_dict)


    @property
    def data(self):
        return self._internal_dict["data"]

    @data.setter
    def data(self, new_data):
        self._internal_dict["data"] = new_data

    @property
    def metadata(self):
        return self._internal_dict["metadata"]

    @metadata.setter
    def metadata(self, new_metadata):
        self._internal_dict["metadata"] = new_metadata







