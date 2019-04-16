from collections.abc import Sequence, Mapping

import pandas

from pyaaas.privacy_models import PrivacyModel


def create_privacy_models_dataframe(privacy_models: Sequence) -> pandas.DataFrame:
    """
    Creates a pandas.DataFrame from Sequence of PrivacyModels objects

    :param privacy_models: Sequence of PrivacyModels
    :return: pandas.DataFrame
    """
    privacy_models_index = []
    privacy_models_values = []

    for model in privacy_models:
        model_index = create_model_indexes(model)
        model_values = create_model_values(model)
        privacy_models_index += model_index
        privacy_models_values += model_values
    index = pandas.MultiIndex.from_tuples(privacy_models_index, names=("privacy_model", "parameter"))
    dataframe = pandas.DataFrame(privacy_models_values, index=index, columns=("value",))
    return dataframe


def create_model_indexes(model: PrivacyModel):
    """
    Creates the indexes for a provided PrivacyModel to be used in a MultiIndex DataFrame
    :param model: PrivacyModel object
    :return: model_index: tuple of tuples containing indexes
    """
    model_index = []
    for key, value in model.items():
        model_index.append((model.name, key))
    return model_index


def create_model_values(model: PrivacyModel):
    """
    Create list of values from the PrivacyModel object
    :param model: PrivacyModel object
    :return: List of values
    """
    model_values = []
    for value in model.values():
        model_values.append(value)
    return model_values


def create_attribute_types_dataframe(attribute_types: Mapping) -> pandas.DataFrame:
    """
    Creates a pandas.Dataframe from a Mapping of attribute_types str:field=str:attribute_type

    :param attribute_types: Mapping str:field=str:attribute_type
    :return: pandas.DataFrame
    """
    attribute_rows = attribute_types.items()
    return pandas.DataFrame(attribute_rows, columns=("field", "type")).set_index("field")


def create_transform_models_dataframe(transform_models):
    """
    Creates a pandas.DataFrame form a Mapping of Transform Models


    :param transform_models: mapping
    :return: pandas.DataFrame
    """
    transform_models_index = []
    transform_models_values = []

    for field, hierarchy in transform_models.items():
        field_index, field_values = _create_index_and_values_for(field, hierarchy)
        transform_models_index += field_index
        transform_models_values += field_values

    index = pandas.MultiIndex.from_tuples(transform_models_index)
    dataframe = pandas.DataFrame(transform_models_values, index=index)
    return dataframe


def _create_index_and_values_for(field, hierarchy):
    transform_model_index = []
    transform_model_values = []

    for level in range(1, _get_hierarchy_levels(hierarchy)):
        model_index = [field]
        level_values = []
        model_index.append(f"level_{level}")
        transform_model_index.append(model_index)
        for row in hierarchy:
            level_values.append(row[level])
        transform_model_values.append(level_values)
    return transform_model_index, transform_model_values


def create_dataframe_with_index_from_mapping(mapping: Mapping, columns: Sequence):
    """
    Convenicence function for easy creation of pandas.DataFrame from Python mapping object
    :param mapping: Mapping object to create pandas.DataFrame from
    :param columns: Columns to use in the DataFrame. First column will be used as index
    :return: pandas.DataFrame
    """
    return pandas.DataFrame(mapping.items(), columns=columns).set_index(columns[0])


def _get_hierarchy_levels(hierarchy):
    return len(hierarchy[0])
