from pyaaas.aaas_connector import AaaSConnector
from pyaaas.dataset import Dataset


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector):
        self._connector = connector(url)

    def anonymize(self, dataset: Dataset, privacy_models):
        data_dict = dataset._payload()
        models = []
        for model in list(privacy_models):
            models.append(model._payload())
        data_dict["privacyModels"] = models
        return self._connector.anonymize_data(data_dict)

    def risk_profile(self, dataset: Dataset):
        data_dict = dataset._payload()
        return self._connector.risk_profile(data_dict)

