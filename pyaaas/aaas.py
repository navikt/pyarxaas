import json

import requests

from pyaaas.aaas_connector import AaaSConnector
from pyaaas.dataset import Dataset
from pyaaas.risk_profile import RiskProfile


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector, client=None):
        self._connector = connector(url, client=client)

    def anonymize(self, dataset: Dataset, privacy_models):
        data_dict = dataset._payload()
        models = []
        for model in list(privacy_models):
            models.append(model._payload())
        data_dict["privacyModels"] = models
        response = self._connector.anonymize_data(data_dict)
        self._throw_exeption_on_error_response(response)
        json_string = response.text
        response_dict = json.loads(json_string)
        return Dataset(response_dict["anonymizeResult"]["data"])

    def risk_profile(self, dataset: Dataset):
        data_dict = dataset._payload()
        response = self._connector.risk_profile(data_dict)
        self._throw_exeption_on_error_response(response)
        metric_dict = json.loads(response.text)
        return RiskProfile(metric_dict)

    @staticmethod
    def _throw_exeption_on_error_response(response: requests.Response) -> None:
        # if status code does not start with 2xx throw exception
        if not str(response.status_code)[0] == "2":
            raise SystemError(response.text)