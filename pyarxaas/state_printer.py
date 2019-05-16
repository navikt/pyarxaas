from collections.abc import Mapping, Callable
from IPython.core import display as ICD
import pandas


def print_privacy_models(models: Mapping, printer: Callable) -> pandas.DataFrame:
    """
    Prints out a human readable view of the provided Privacy Models

    :param models: collection of Privacy models
    :param printer: callable
    :return: None
    """
    for model in models.values():
        return _model_to_dataframe(model)


def print_mapping(name_data_mapping: Mapping):
    """
    Prints the current content of the payload object to stdout

    :param name_data_mapping: Mapping object name:data
    :return: None
    """

    for name, dataframe in name_data_mapping.items():
        print(name)
        print(dataframe)
        print("-"*40 + "\n")


def jupyter_print_mapping(name_dataframe_mapping: Mapping):
    """
    Print the provided name_dataframe_mapping in a J

    :param name_dataframe_mapping:
    :return:
    """
    for name, dataframe in name_dataframe_mapping.items():
        print(name)
        ICD.display(dataframe)
        print("-"*40)


def _model_to_dataframe(model):
    return pandas.DataFrame(model.items())
