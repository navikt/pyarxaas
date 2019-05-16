import json
from collections.abc import Mapping

from pyaaas.models.request_builder import RequestBuilder
from pyaaas.arxaas_connector import ARXaaSConnector
from pyaaas.models.anonymize_result import AnonymizeResult
from pyaaas.models.dataset import Dataset
from pyaaas.models.risk_profile import RiskProfile


class ARXaaS:
    """
    Represents the connection to ARXaaS. All public methods result in a call to the service.
    """

    def __init__(self, url: str, connector=ARXaaSConnector, client=None):
        self._connector = connector(url, client=client)
        self._connector.test_connection()

    def anonymize(self, dataset: Dataset, privacy_models,suppression_limit: float = None) -> AnonymizeResult:
        """
        Attempt to anonymize a dataset with provided privacy models

        :param dataset: Dataset to be anonymized
        :param privacy_models: privacy models to be used in the anonymization
        :param suppression_limit: suppression limit to be used in the anonymization
        :return: Dataset with anonymized data
        """
        request_payload = self._anonymize_payload(dataset, privacy_models, suppression_limit)
        response = self._anonymize(request_payload)
        return self._anonymize_result(response)

    def _anonymize_payload(self, dataset, privacy_models, suppression_limit) -> Mapping:
        """
        Creates a anonymize payload to be sent to the backend

        :param dataset: Dataset to be anonymized
        :param privacy_models: privacy models to be used in the anonymization
        :param suppression_limit: suppression limit to be used in the anonymization
        :return: Mapping payload
        """

        return RequestBuilder(dataset)\
            .add_privacy_models(privacy_models)\
            .add_suppression_limit(suppression_limit)\
            .build_anonymize_request()

    def _anonymize(self, payload):
        """
        Passes the payload to the connector for anonymization
        :param payload: Mapping matching the service anonymize json schema
        :return:
        """
        response = self._connector.anonymize_data(payload)
        return response

    def _anonymize_result(self, response):
        """
        Creates the result to be delivered back to the caller

        :param response:
        :return:
        """
        json_string = response.text
        response_dict = json.loads(json_string)
        attributes = self._attributes(response_dict)
        dataset = Dataset(response_dict["anonymizeResult"]["data"], attributes)
        risk_profile = RiskProfile(response_dict["riskProfile"])
        anon_status = response_dict["anonymizeResult"]["anonymizationStatus"]
        anonymization_metrics = response_dict["anonymizeResult"]["metrics"]
        return AnonymizeResult._from_response(dataset, risk_profile, anonymization_metrics, anon_status)

    def risk_profile(self, dataset: Dataset) -> RiskProfile:
        """
        Creates a risk profile for a provided Dataset

        RiskProfile contains:
         - re-identifiaction risks
         - distributed risk

        :param dataset: Dataset to create a risk profile for
        :return: RiskProfile
        """

        analyze_request = self._risk_profile_payload(dataset)
        response = self._risk_profile(analyze_request)
        metric_dict = json.loads(response.text)
        return RiskProfile(metric_dict)

    def _risk_profile_payload(self, dataset):
        """
        Creates a risk profile payload to be sent to the backend

        :param dataset: Dataset to be analyzed
        :return: Mapping payload
        """

        return RequestBuilder(dataset).build_analyze_request()

    def _risk_profile(self, data_dict):
        """
        Passes the payload to the connector for risk profiling
        :param payload: Mapping matching the service anonlyze json schema
        :return: Response
        """

        response = self._connector.risk_profile(data_dict)
        return response

    def _attributes(self, response_dict):
        raw = response_dict["anonymizeResult"]["attributes"]
        attribute_dict = {attribute["field"]: attribute["attributeTypeModel"] for attribute in raw}
        return attribute_dict

    def hierarchy(self, redaction_builder, column):
        """
        Creates a value generalization hierarchy with the passed in builder for the passed in column.


        :param redaction_builder: a Hierarchy builder instance
        :param column: a list of values
        :return: list[list] containing the created hierarchy
        """

        request = redaction_builder._request_payload()
        request["column"] = column
        response = self._connector.hierarchy(request)
        response_dict = json.loads(response.text)
        return response_dict["hierarchy"]