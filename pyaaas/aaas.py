import sys
import os
from collections.abc import MutableMapping, Sequence, Callable
import json

import requests

from pyaaas.aaas_connector import AaaSConnector
from pyaaas.models.anonymize_payload import AnonymizePayload
from pyaaas.models.privacy_models import PrivacyModel
from pyaaas.models.anonymize_result import AnonymizeResult
from pyaaas.state_printer import jupyter_print_mapping, print_mapping
from pyaaas.attribute_type import AttributeType
from pyaaas.converters import create_privacy_models_dataframe,create_attribute_types_dataframe,\
    create_transform_models_dataframe


class AaaS:
    """ ARX Web Service Connector object for connecting to the Web API.
        Add data to be anonymized, and configure anonymizaton
     """

    def __init__(self, url: str=None):
        """
        :param url: url to AaaS Web Service
        """

        # Connect to endpoint
        if url is None:
            url = self._get_url_from_env()
        self._conn = AaaSConnector(base_url=url)

        self._payload = AnonymizePayload()

    def set_attribute_type(self, field, attribute_type=None):
        """
        Sett atttribute type for one or several fields

        :param field: field(s) in the dataframe
        :param attribute_type: the attribute type for the field(s)
        :return: None
        """
        if isinstance(field, Sequence):
            for c_field in field:
                self._payload.add_attribute_type(c_field, attribute_type)
        if isinstance(field, MutableMapping):
            for c_field, attribute_type in field.items():
                if isinstance(attribute_type, AttributeType):
                    self._payload.add_attribute_type(c_field, attribute_type.value)
                else:
                    self._payload.add_attribute_type(c_field, attribute_type)
        else:
            self._payload.add_attribute_type(field, attribute_type)

    def set_hierarchy(self, field, hierarchy_data):
        """
        Set Transform Model Hierarchy for a field in the dataframe

        :param field: field in the dataframe
        :param hierarchy_data: a Hierarchy object
        :return: None
        """
        self._payload.add_hierarchy(field, hierarchy_data)

    def set_model(self, model: PrivacyModel):
        """
        Set a PrivacyModel for the anonymization action

        :param model: PrivacyModel to apply to the dataframe
        :return: None
        """
        self._payload.add_model(model.name, model)

    def set_data(self, data):
        """
        Set the data to be anonymized or analyzed

        :param data: data (DataFrame,  CSV str)
        :return: None
        """
        self._payload.data = data

    def anonymize(self) -> AnonymizeResult:
        """
        Run Anonymization on the currently applied configurations and data

        :return: AnonymizationResult wuith the result from the AaaS Web Service
        """
        result = self._conn.anonymize_data(self._payload.to_dict())
        self._throw_exeption_on_error_response(result)

        result_dict = json.loads(result.text)
        return AnonymizeResult(result_dict)

    def describe(self, printer: Callable = print_mapping) -> None:
        """
        Describes the current state of the AaaS object to the user
        Default behaviour is to print the current state of the payload object to the user.

        :param printer: Callable object called to describe the payload state
        """
        privacy_models_dataframe = create_privacy_models_dataframe(self.payload.models.values())
        attribute_types_dataframe = create_attribute_types_dataframe(self.payload.attribute_types)
        transform_models_dataframe = create_transform_models_dataframe(self.payload.hierarchy)
        name_dataframe_mapping = {"Privacy Models": privacy_models_dataframe,
                                  "Attribute Types": attribute_types_dataframe,
                                  "Transform Models": transform_models_dataframe}
        printer(name_dataframe_mapping)

    @staticmethod
    def _get_url_from_env():
        try:
            return os.environ["AAAS_URL"]
        except KeyError:
            raise EnvironmentError("No AAAS_URL set in the environment")


    @staticmethod
    def _throw_exeption_on_error_response(response: requests.Response) -> None:
        if response.status_code != 200:
            raise SystemError(response.text)



