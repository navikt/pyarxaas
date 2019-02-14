from collections.abc import Sequence, Mapping

import pandas


def create_privacy_models_dataframe(privacy_models: Sequence) -> pandas.DataFrame:
    """
    Creates a pandas.DataFrame from Sequence of PrivacyModels objects

    :param privacy_models: Sequence of PrivacyModels
    :return: pandas.DataFrame
    """
    privacy_models_index = []
    privacy_models_values = []

    for model in privacy_models:
        model_index =[model.name]
        for key, value in model.items():
            model_index.append(key)
            privacy_models_values.append(value)
        privacy_models_index.append(model_index)

    index = pandas.MultiIndex.from_tuples(privacy_models_index, names=("privacy_model", "parameter"))
    dataframe = pandas.DataFrame(privacy_models_values, index=index, columns=("value",))
    return dataframe


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

        for level in range(1, len(hierarchy[0])):
            model_index = [field]
            level_values = []
            model_index.append("level_" + str(level))
            transform_models_index.append(model_index)
            for row in hierarchy:
                level_values.append(row[level])
            transform_models_values.append(level_values)

    index = pandas.MultiIndex.from_tuples(transform_models_index)
    dataframe = pandas.DataFrame(transform_models_values, index=index)
    return dataframe
