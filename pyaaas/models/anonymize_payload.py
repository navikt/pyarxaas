from collections.abc import MutableMapping
from typing import Iterator
from json import JSONEncoder


class AnonymizePayload(MutableMapping):
    """
    Anonymization data and meta data container
    """

    def __init__(self, data=None, meta_data: MutableMapping=None):
        if meta_data is None:
            meta_data = {"attribute_type": {}, "hierarchy": {}, "models": {}}
        self._internal_dict = {"data": data, "metadata": meta_data}

    def __setitem__(self, k, v) -> None:
        self._internal_dict[k] = v

    def __delitem__(self, v) -> None:
        del self._internal_dict[v]

    def __getitem__(self, k):
        return self._internal_dict[k]

    def __len__(self) -> int:
        return len(self._internal_dict)

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

    @property
    def attribute_type(self):
        return self._internal_dict["metadata"]["attribute_type"]

    @property
    def models(self):
        return self._internal_dict["metadata"]["models"]

    @property
    def hierarchy(self):
        return self._internal_dict["metadata"]

    def add_attribute_type(self, field, value):
        self._internal_dict["metadata"]["attribute_type"][field] = value

    def add_hierarchy(self, field, value):
        self._internal_dict["metadata"]["hierarchy"][field] = value

    def add_model(self, field, value):
        self._internal_dict["metadata"]["models"][field] = value

    def to_dict(self) -> dict:
        payload_dict = {**self._internal_dict}
        models = {}
        for key, value in self.metadata["models"].items():
            model_dict = {**value}
            models[key] = model_dict
        payload_dict["metadata"]["models"] = models
        converted = _convert_payload_to_backed_schema(payload_dict)
        return converted



class PayloadJSONConverter(JSONEncoder):

    def default(self, anon_payload):
        result_dict = {**anon_payload}
        models = {}
        for key, value in anon_payload.metadata["models"].items():
            model_dict = {**value}
            models[key] = model_dict
        result_dict["metadata"]["models"] = models
        result_dict = _convert_payload_to_backed_schema(result_dict)
        return result_dict




def _convert_payload_to_backed_schema(payload):
    payload["metaData"] = payload["metadata"]
    payload["metaData"]["sensitivityList"] = payload["metaData"]["attribute_type"]
    del payload["metadata"]
    del payload["metaData"]["attribute_type"]
    return payload


