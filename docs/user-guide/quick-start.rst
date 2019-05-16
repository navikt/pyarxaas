.. _quick-start:


Quick Start
===========

This page gives a good introduction in how to get started with PyARXaaS

**First, make sure that:**

- PyARXaaS is installed
- PyARXaaS is up-to-date
- You have a tabular dataset to use
- You hava a running ARXaaS instance to connect to.
    - Instructions on how to run ARXaaS can be found here: https://github.com/oslomet-arx-as-a-service/ARXaaS/blob/master/README.md
- If you are going to anonymize a dataset, you need to have the required hierarchies. See anonymize section for more information

Let’s get started with some simple examples.

Analyze the risk of a dataset
-----------------------------
Analyze the risk of a dataset using PyARXaaS is very simple.

1. **Begin by importing the Dataset class and pandas which we are going to use to create a** :ref:`dataset` ::

    from pyarxaas import Dataset
    import pandas as pd

 Then we create a Dataset from a local csv file

 .. note:: The dataset in this example contains the columns/fields **id, name, gender**

 ::

    dataframe = pd.read_csv("data.csv", sep=";")
    # create Dataset
    dataset = Dataset.from_pandas(dataframe)

 *The Dataset class encapsulates the raw data, attribute types of the dataset fields and hierarchies*

2. **Then we set the**  :ref:`attribute_type` **for the Dataset fields.** ::

    # import the attribute_type module
     from pyarxaas import AttributeType

    # set attribute type
    dataset.set_attribute_type(AttributeType.QUASIIDENTIFYING, 'name', 'gender')
    dataset.set_attribute_type(AttributeType.IDENTIFYING, 'id')

3. **To make a call to the ARXaaS instance we need to make a instance of the** :ref:`arxaas` **class.**

 The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally. ::

    # import the ARXaaS class
    from pyarxaas import ARXaaS

    # establishing a connection to the ARXaaS service using a URL
    arxaas = ARXaaS("http://localhost:8080")

4. **After the** :ref:`arxaas` **object is created we can use it to call the ARXaaS instance to make a** :ref:`risk_profile` **for our Dataset.** ::

    # get the risk profle of the dataset
    risk_profile = arxaas.risk_profile(dataset)



 The :ref:`risk_profile` contains two properties; re-indentification risks and distributed risks.
 The two properties contains the different risks and the distribution of risks for the :ref:`dataset`. ::

    # get risk metrics as a dictionary
    re_indentifiation_risk = risk_profile.re_identification_risk
    distribution_of_risk = risk_profile.distribution_of_risk

    # get risk metrivs as pandas.DataFrame
    re_i_risk_df = risk_profile.distribution_of_risk_dataframe()
    dist_risk_df = risk_profile.distribution_of_risk_dataframe()




Anonymize a dataset
-----------------------------
Anonymizing a dataset using PyARXaaS.

1. **Begin by importing the Dataset class and pandas which we are going to use to create a Dataset** ::

        from pyarxaas import Dataset
        import pandas as pd


2. **Same as when in analyze we set the attribute type for the dataset fields**::

    # import the attribute_type module
     from pyarxaas import AttributeType

    # set attribute type
    dataset.set_attributes(AttributeType.QUASIIDENTIFYING, 'name', 'gender')
    dataset.set_attributes(AttributeType.IDENTIFYING, 'id')

3. **In addition to setting attribute types we need to provide Transformation Models known as hierarchies for the dataset fields/columns with type AttributeType.QUASIIDENTIFYING**
Hierarchies can be added as pandas.DataFrame objects::

    # importing the hierarchies from a local csv file. Specify the file path as the first parameter
    id_hierarchy = pd.read_csv("id_hierarchy.csv", header=None)
    name_hierarchy = pd.read_csv("name_hierarchy.csv", header=None)

    # setting the imported csv file. Specify the column name as the fist parameter, and the hierarchy as the second parameter
    dataset.set_hierarchy('id', id_hierarchy)
    dataset.set_hierarchy('name', name_hierarchy)


4. **When anonymizing we need to supply a** :ref:`privacy_model` **for ARXaaS to run on the dataset. You can read more about the models here** `ARX Privacy Models <https://arx.deidentifier.org/overview/privacy-criteria/>`_ ::

    # importing the privacy_models module
    from pyarxaas.privacy_models import KAnonymity

    # creating a privacy_models object
    kanon = KAnonymity(4)

5. **To make a call to the ARXaaS instance we need to make a instance of the AaaS class. The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally.** ::


    # import the aaas module
    from pyarxaas import ARXaaS

    # establishing a connection to the ARXaaS service using the URL
    arxaas = ARXaaS("http://localhost:8080")

6. **After the** :ref:`arxaas` **object is created we can use it to call the ARXaaS instance. Back if the anonymization is successful we receive an** :ref:`anonymize_result` ::


    # specify the dataset as the first parameter, and privacy model list as the second paramter
    anonymize_result = arxxaas.anonymize(dataset, [kanon])

:ref:`anonymize_result` contains the new :ref:`dataset`, the :ref:`risk_profile` for the new , the :ref:`dataset`,
the anonymization status for the :ref:`dataset` and :ref:`anonymization_metrics` which contains metrics regarding the anonymzation performed on the dataset. ::

    # get the new dataset
    anonymized_dataset = anonymize_result.dataset
    anon_dataframe = anonymized_dataset.to_dataframe()

    # get the risk profile for the new dataset
    anon_risk_profile = anonymize_result.risk_profile

    # get risk metrics as a dictionary
    re_indentifiation_risk = anon_risk_profile.re_identification_risk
    distribution_of_risk = anon_risk_profile.distribution_of_risk

    # get risk metrivs as pandas.DataFrame
    re_i_risk_df = anon_risk_profile.distribution_of_risk_dataframe()
    dist_risk_df = anon_risk_profile.distribution_of_risk_dataframe()

    # get the anonymiztion metrics
    anon_metrics = anonymize_result.anonymization_metrics

