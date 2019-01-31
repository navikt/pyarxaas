from collections.abc import MutableMapping
from typing import Iterator


class AnonymizePayload(MutableMapping):
    """
    Anonymization data and meta data container
    """

    def __init__(self, data=None, meta_data: MutableMapping=None):
        if meta_data is None:
            meta_data = {"attribute_type": {}, "hierarchy": {}, "model": {}}
        self._internal_dict = {"data": data, "metadata": meta_data}

    def __setitem__(self, k, v) -> None:
        self._internal_dict[k] = v

    def __delitem__(self, v) -> None:
        del self._internal_dict[v]

    def __getitem__(self, k):
        return self._internal_dict[k]

    def __len__(self) -> int:
        return  len(self._internal_dict)

    def __iter__(self):
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







