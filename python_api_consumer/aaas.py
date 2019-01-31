import sys
import os
from collections.abc import MutableMapping, Sequence
import csv

from python_api_consumer.aaas_connector import AaaSConnector
from python_api_consumer.models.anonymize_payload import AnonymizePayload


class AaaS:
    """ ARX Web Service Connector object for connecting to the Web API.
        Add data to be anonymized, and configure anonymizaton
     """

    def __init__(self, url: str=None):
        # Connect to endpoint
        if url is None:
            url = self._get_url_from_env()
        self.conn = AaaSConnector(base_url=url)

        self.payload = AnonymizePayload()

    def set_attribute_type(self, fields, value=None):
        if isinstance(fields, Sequence):
            for field in fields:
                self.payload.metadata["attribute_type"][field] = value
        if isinstance(fields, MutableMapping):
            self.payload.metadata["attribute_type"] = value
        else:
            self.payload.metadata["attribute_type"][fields] = value

    def set_hierarchy(self, field, hierarchy_data):
        if isinstance(hierarchy_data, Sequence):
            hierarchy_data = self._list_to_csv_string(hierarchy_data)
        self.payload.metadata["hierarchy"][field] = hierarchy_data

    def set_model(self, model):
        self.payload.metadata["model"][model.name] = model

    def set_data(self, data):
        self.payload.data = data

    def anonymize(self) -> MutableMapping:
        return self.conn.anonymize_data(self.payload)


    @staticmethod
    def _list_to_csv_string(list):
        csv_string = ""
        for sublist in list:
            substring = ";".join(sublist)
            substring += ";\n"
            csv_string += substring
        return csv_string


    @staticmethod
    def _get_url_from_env():
        try:
            return os.environ["AAAS_URL"]
        except KeyError:
            raise EnvironmentError("No AAAS_URL set in the environment")

