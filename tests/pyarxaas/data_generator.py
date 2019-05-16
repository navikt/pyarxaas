# module for collection of test data generating functions and classes
import json
from os import path
from pyarxaas.models.anonymize_result import AnonymizeResult
from pyarxaas.models.attribute_type import AttributeType
from pyarxaas.models.dataset import Dataset
from pyarxaas.models.risk_profile import RiskProfile

here = path.abspath(path.dirname(__file__))


def response_dict(file):
    with open(path.join(here, file), encoding="utf-8") as json_file:
        return json.load(json_file)


def analyze_response():
    return response_dict("test_data/analyze_response_test_data.json")


def anonymize_response():
    return response_dict("test_data/anonymize_response_test_data.json")


def id_name_dataset() -> Dataset:
    test_data = [['id', 'name'],
                      ['0', 'Viktor'],
                      ['1', 'Jerry']]
    test_attribute_type_mapping = {'id': AttributeType.IDENTIFYING,
                                        'name': AttributeType.QUASIIDENTIFYING}
    return Dataset(test_data, test_attribute_type_mapping)


def raw_anonymization_metrics():
    metrics = anonymize_response()["anonymizeResult"]["metrics"]
    return metrics


def risk_profile() -> RiskProfile:
    raw_risk_profile = analyze_response()
    return RiskProfile(raw_risk_profile)
