from pyaaas.aaas_connector import AaaSConnector
from pyaaas.dataset import Dataset


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector):
        self._connector = connector(url)

    def analyze(self, dataset: Dataset):
        self._connector.analyze(self._convert_to_payload(dataset))

    def _convert_to_payload(self, dataset):
        payload = {}
        dataset_dict = dataset.to_dict()
        payload["data"] = dataset_dict["data"]
        payload["attributeTypes"] = dataset_dict["attribute_types"]
        return payload

