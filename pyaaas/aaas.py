from pyaaas.aaas_connector import AaaSConnector
from pyaaas.dataset import Dataset


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector):
        self._connector = connector(url)

    def risk_profile(self, dataset: Dataset):
        data_dict = dataset._to_payload()
        return self._connector.risk_profile(data_dict)

