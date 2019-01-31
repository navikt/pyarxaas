import sys
import os
from collections.abc import MutableMapping, Sequence
import json

from python_api_consumer.aaas_connector import AaaSConnector
from python_api_consumer.models.anonymize_payload import AnonymizePayload, PayloadJSONConverter
from python_api_consumer.models.privacy_models import PrivacyModel


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

    def set_attribute_type(self, field, value=None):
        if isinstance(field, Sequence):
            for c_field in field:
                self.payload.add_attribute_type(c_field, value)
        if isinstance(field, MutableMapping):
            for c_field, value in field.items():
                self.payload.add_attribute_type(c_field, value)
        else:
            self.payload.add_attribute_type(field, value)

    def set_hierarchy(self, field, hierarchy_data):
        self.payload.add_hierarchy(field, hierarchy_data)

    def set_model(self, model: PrivacyModel):
        self.payload.add_model(model.name, model)

    def set_data(self, data):
        self.payload.data = data

    def anonymize(self) -> MutableMapping:
        return self.conn.anonymize_data(self.payload.to_dict())


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



