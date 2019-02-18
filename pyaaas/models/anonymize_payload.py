from collections.abc import MutableMapping
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from pandas import DataFrame


class AnonymizePayload(MutableMapping):
    """
    Anonymization data and meta data container
    """

    def __init__(self, data=None, meta_data: MutableMapping=None):
        if meta_data is None:
            meta_data = {"attribute_type": {},
                         "hierarchy": {},
                         "models": {}
                         }
        self._payload_dict = {"data": data,
                               "metadata": meta_data
                              }

    def __setitem__(self, k, v) -> None:
        self._payload_dict[k] = v

    def __delitem__(self, v) -> None:
        del self._payload_dict[v]

    def __getitem__(self, k):
        return self._payload_dict[k]

    def __len__(self) -> int:
        return len(self._payload_dict)

    def __iter__(self):
        return iter(self._payload_dict)

    @property
    def data(self):
        """ User provided data to be anonymised """
        return self._payload_dict["data"]

    @data.setter
    def data(self, new_data):
        if isinstance(new_data, DataFrame):
            new_data = new_data.to_csv(sep=",", index=False)
        self._payload_dict["data"] = new_data

    @property
    def metadata(self):
        """ metadata about the user provided data"""
        return self._payload_dict["metadata"]

    @metadata.setter
    def metadata(self, new_metadata):
        self._payload_dict["metadata"] = new_metadata

    @property
    def attribute_types(self):
        """ ARX Attribute types for the data fields"""
        return self._payload_dict["metadata"]["attribute_type"]

    @property
    def models(self):
        """ PrivacyModels to be used in the anonymization process"""
        return self._payload_dict["metadata"]["models"]

    @property
    def hierarchy(self):
        return self._payload_dict["metadata"]["hierarchy"]

    def add_attribute_type(self, field, value):
        self._payload_dict["metadata"]["attribute_type"][field] = value

    def add_hierarchy(self, field, value):
        self._payload_dict["metadata"]["hierarchy"][field] = value

    def add_model(self, field, value):
        self._payload_dict["metadata"]["models"][field] = value

    def to_dict(self) -> dict:
        payload_dict = {**self._payload_dict}
        models = {}
        for key, value in self.metadata["models"].items():
            model_dict = {**value}
            models[key] = model_dict
        payload_dict["metadata"]["models"] = models
        converted = _convert_payload_to_backend_schema(payload_dict)
        return converted


def _convert_payload_to_backend_schema(payload):
    payload["metaData"] = payload["metadata"]
    payload["metaData"]["sensitivityList"] = payload["metaData"]["attribute_type"]
    del payload["metadata"]
    del payload["metaData"]["attribute_type"]
    return payload


