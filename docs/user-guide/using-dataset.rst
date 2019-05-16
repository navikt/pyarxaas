.. _using_dataset:

Using the Dataset class
=======================

The :ref:`dataset` class is the represents a tabular dataset containing continuous or categorical attributes.
Additionally each attribute has a :ref:`attribute_type` describing the re-identification risk and sensitivity associated with
the attribute.

In the case where a attribute is Quasi-identifying a hierarchy object can be added (Read more about hierarchies here).

:ref:`dataset` contains

- Tabular dataset
- :ref:`attribute_type` for the dataset fields/attributes
- (optional) hierarchies for the quasi-identifying attributes


Construction
------------
A :ref:`dataset` object can be made from a pandas.DataFrame or a python dict using the constructor class methods.

**From Python dictionary** ::

    data_dict = {"id": [1,2,3], "name": ["Mike", "Max", "Larry"]}
    new_dataset = Dataset.from_dict(data_dict)



**From pandas.DataFrame** ::

    dataframe = pd.read_csv("data.csv", sep=";")
    new_dataset = Dataset.from_pandas(dataframe)


Covert Dataset to other types
-----------------------------
The Dataset class has convenient methods for converting the tabular dataset back to usefull datastructures

**To pandas.DataFrame**
Note: When you create a pandas.DataFrame from a Dataset only the tabular data is included.
The :ref:`attribute_type` information and hierarchies are lost. ::

    data_dict = {"id": [1,2,3], "name": ["Mike", "Max", "Larry"]}
    new_dataset = Dataset.from_dict(data_dict)
    dataframe = new_dataset.to_dataframe()
    #    id   name
    #0   1   Mike
    #1   2    Max
    #2   3  Larry

Mutation
---------

--------------
Attribute type
--------------

The default :ref:`attribute_type` for attributes in a Dataset is :ref:`attribute_type`.QUASIIDENTIFYING. The default is set to
quasi-identifying so that new users will error on the safe side. You can change the type of a attribute with the set_attribute_type() method.::

    from pyarxaas import AttributeType
    new_dataset.set_attribute_type(AttributeType.IDENTIFYING, "id")

Above we have changed the :ref:`attribute_type` of the :ref:`dataset` to :ref:`attribute_type`.IDENTIFYING. This signals that the *id* attribute is a directly identifying attribute in this :ref:`dataset`.
*id* will be treated as such if anonymization is applied to the :ref:`dataset`.

Read more about the different Attribute types here: :ref:`attribute_type`

It is possible to pass *n* attributes following the :ref:`attribute_type` parameter to set the attribute type to all the attribute. ::

    # Here id and name are marked as insensitive attributes
    new_dataset.set_attribute_type(AttributeType.INSENSITIVE, "id", "name")


------------
Hierarchies
------------

Hierarchy also referred to as *generalization hierarchies* represented either as pandas.DataFrames or a regular Python
list, are the strategies ARXaaS will use when attempting to anonymize the dataset. Read more about them :ref:`create_hierarchies`.

**Setting a hierarchy on a Dataset attribute** ::

    id_hierarchy = [["1", "*"], ["2", "*"], ["3", "*"]]
    dataset.set_hierarchy("id", id_hierarchy)

You can also set several hierarchies in one call with the .set_hierarchies(hierarchies) method. ::

    id_hierarchy = [["1", "*"], ["2", "*"], ["3", "*"]]
    job_hierarchy = [["plumber", "manual-labour", "*"],
                     ["hairdresser", "service-industry", "*"]]
    hierarchies = {"id": id_hierarchy, "job": job_hierarchy}
    dataset.set_hierarchies(hierarchies)

