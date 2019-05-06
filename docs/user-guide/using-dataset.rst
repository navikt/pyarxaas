

Using the Dataset class
=======================

The :ref:`dataset` class is the represents a tabular dataset containing continuous or categorical attributes.
Additionally each attribute has a :ref:`attribute_type` describing the re-identification risk and sensitivity associated with
the attribute.

In the case where a attribute is Quasiidentifying a hierarchy object can be added (Read more about hierarchies here).

:ref:`dataset` contains

- Tabular dataset
- :ref:`attribute_type` for the dataset fields/attributes
- (optional) hierarchies for the quasiidentfiying attributes


Construction
------------
A :ref:`dataset` object can be made from a pandas.DataFrame or a python dict using the constructor class methods.

**From Python dictionary** ::

    data_dict = {"id": [1,2,3], "name": ["Mike", "Max", "Larry"]}
    new_dataset = Dataset.from_dict(data_dict)



**From pandas.DataFrame** ::

    dataframe = pd.read_csv("data.csv", sep=";")
    new_dataset = Dataset.from_pandas(dataframe)


Covert Dataset
--------------
The Dataset class has convenient methods for converting the tabular dataset back to usefull datastructures

**To pandas.DataFrame** ::

    data_dict = {"id": [1,2,3], "name": ["Mike", "Max", "Larry"]}
    new_dataset = Dataset.from_dict(data_dict)
    dataframe = new_dataset.to_dataframe()
    #    id   name
    #0   1   Mike
    #1   2    Max
    #2   3  Larry
