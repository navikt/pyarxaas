

class AaaS:
    """ ARX Web Service Connector object for connecting to the Web API.
        Add data to be anonymized, and configure anonymizaton
     """

    def __init__(self, url:str):
        self._endpoint_url = url

    def add_data(self, data):
        self._data = data

    def add_config(self, config):
        self._config = config



