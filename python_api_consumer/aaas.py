import sys
import os
from collections.abc import MutableMapping

from python_api_consumer.aaas_connector import AaaSConnector
from python_api_consumer.models.anonymize_payload import AnonymizePayload

class AaaS:
    """ ARX Web Service Connector object for connecting to the Web API.
        Add data to be anonymized, and configure anonymizaton
     """

    def __init__(self, url: str=None):

        if url is None:
            url = self._get_url_from_env()

        self.conn = AaaSConnector(base_url=url)

        self._data = {}

    def add_data(self, data):
        self._data = data

    def anonymize(self) -> MutableMapping:
        return self.conn.anonymize_data(self._data)


    @staticmethod
    def _get_url_from_env():
        try:
            return os.environ["AAAS_URL"]
        except KeyError:
            raise EnvironmentError("No AAAS_URL set in the environment")
