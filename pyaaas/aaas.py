from pyaaas.aaas_connector import AaaSConnector
from pyaaas.dataset import Dataset


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector):
        self._connector = connector(url)

    def analyze(self, dataset: Dataset):
        self._connector.analyze(dataset.to_dict())

