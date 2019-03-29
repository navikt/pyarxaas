import json
from collections.abc import Mapping

import requests

from pyaaas.aaas_connector import AaaSConnector
from pyaaas.anonymize_result import AnonymizeResult
from pyaaas.dataset import Dataset
from pyaaas.risk_profile import RiskProfile


class AaaS:
    """
    Understands connection to ARXaaS
    """

    def __init__(self, url: str, connector=AaaSConnector, client=None):
        self._connector = connector(url, client=client)

    def anonymize(self, dataset: Dataset, privacy_models):
        """
        Attempt to anonymize a dataset with provided privacy models

        :param dataset: Dataset to be anonymized
        :param privacy_models: privacy models to be used in the anonymization
        :return: Dataset with anonymized data
        """
        payload = self.anonymize_payload(dataset, privacy_models)
        response = self._anonymize(payload)
        return self.anonymize_result(response)

    def anonymize_payload(self, dataset, privacy_models) -> Mapping:
        """
        Creates a anonymize payload to be sent to the backend

        :param dataset: Dataset to be anonymized
        :param privacy_models: privacy models to be used in the anonymization
        :return: Mapping payload
        """
        data_dict = dataset._payload()
        models = []
        for model in list(privacy_models):
            models.append(model._payload())
        data_dict["privacyModels"] = models
        return data_dict

    def _anonymize(self, payload):
        """
        Passes the payload to the connector for anonymization
        :param payload: Mapping matching the service anonymize json schema
        :return:
        """
        response = self._connector.anonymize_data(payload)
        self._throw_exeption_on_error_response(response)
        return response

    def anonymize_result(self, response):
        """
        Creates the result to be delivered back to the caller

        :param response:
        :return:
        """
        json_string = response.text
        response_dict = json.loads(json_string)
        dataset = Dataset(response_dict["anonymizeResult"]["data"])
        risk_profile = RiskProfile(response_dict["afterAnonymizationMetrics"])
        raw_metrics = {"anonymization_status": response_dict["anonymizeResult"]["anonymizationStatus"]}
        raw_metrics.update(response_dict["anonymizeResult"]["statistics"])
        return AnonymizeResult._from_response(dataset, risk_profile, raw_metrics)

    def risk_profile(self, dataset: Dataset):
        """
        Creates a risk profile for a provided Dataset

        RiskProfile contains:
         - re-identifiaction risks
         - distributed risk

        :param dataset: Dataset to create a risk profile for
        :return: RiskProfile
        """

        data_dict = dataset._payload()
        response = self._risk_profile(data_dict)
        metric_dict = json.loads(response.text)
        return RiskProfile(metric_dict)

    def _risk_profile(self, data_dict):
        """
        Passes the payload to the connector for risk profiling
        :param payload: Mapping matching the service anonlyze json schema
        :return: Response
        """

        response = self._connector.risk_profile(data_dict)
        self._throw_exeption_on_error_response(response)
        return response

    @staticmethod
    def _throw_exeption_on_error_response(response: requests.Response) -> None:
        # if status code does not start with 2xx throw exception
        if not str(response.status_code)[0] == "2":
            raise SystemError(response.text)