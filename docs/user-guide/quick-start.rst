.. _quick-start:


Quick Start
===========

This page gives a good introduction in how to get started with PyAaaS

**First, make sure that:**

- PyAaaS is installed
- PyAaaS is up-to-date
- You have a tabular dataset to use
- You hava a running ARXaaS instance to connect to
- If you are going to anonymize a dataset, you need to have the required hierarchies. See anonymize section for more information

Let’s get started with some simple examples.

Analyze the risk of a dataset
-----------------------------
Analyze the risk of a dataset using PyAaaS is very simple.

1. **Begin by importing the Dataset class and pandas which we are going to use to create a** :ref:`dataset` ::

    from pyaaas.dataset import Dataset
    import pandas as pd

 Then we create a Dataset from a local csv file

 .. note:: The dataset in this example contains the columns/fields **id, name, gender**

 ::

    dataframe = pd.read_csv("data.csv", sep=";")
    # create Dataset
    dataset = Dataset.from_pandas(dataframe)

 *The Dataset class encapsulates the raw data, attribute types of the dataset fields and hierarchies*

2. **Then we set the**  :ref:`attribute_type` **for the Dataset fields.** ::

    # set attribute type
    dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
    dataset.set_attribute('id', AttributeType.IDENTIFYING)


3. **To make a call to the ARXaaS instance we need to make a instance of the** :ref:`aaas` **class.**

 The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally. ::

    from pyaaas.aaas import AaaS
    aaas = AaaS("http://localhost:8080")

4. **After the** :ref:`aaas` **object is created we can use it to call the ARXaaS instance to make a** :ref:`risk_profile` **for our Dataset.** ::

    # get the risk profle of the dataset
    risk_profile = aaas.risk_profile(dataset)



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
Anonymize a dataset using PyAaaS is also very simple.

1. **Begin by importing the Dataset class and pandas which we are going to use to create a Dataset** ::

        from pyaaas.dataset import Dataset
        import pandas as pd


2. **Same as when in analyze we set the attribute type for the dataset fields**::

    # set attribute type
    dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
    dataset.set_attribute('id', AttributeType.IDENTIFYING)

3. **In addtion to setting attribute types we need to provide Transformation Models known as hierarchies for the dataset fields/columns with type AttributeType.QUASIIDENTIFYING**
 Hierarchies can be added as pandas.DataFrame objects::

    id_hierarchy = pd.read_csv("id_hierarchy.csv", header=None)
    dataset.set_hierarchy('id', id_hierarchy)

    name_hierarchy = pd.read_csv("name_hierarchy.csv", header=None)
    dataset.set_hierarchy('name', name_hierarchy)


4. **When anonymizing we need to supply a** :ref:`privacy_model` **for ARXaaS to run on the dataset. You can read more about the models here** `ARX Privacy Models <https://arx.deidentifier.org/overview/privacy-criteria/>` ::

    from pyaaas.model.privacy_models import KAnonymity
    kanon = KAnonymity(4)

5. **To make a call to the ARXaaS instance we need to make a instance of the AaaS class. The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally.** ::

    from pyaaas.aaas import AaaS
    aaas = AaaS("http://localhost:8080")

6. **After the** :ref:`aaas` **object is created we can use it to call the ARXaaS instance. Back if the anonymization is succesfull we receceive an** :ref:`anonymize_result` ::

    anonymize_result = aaas.anonymize(dataset, [kanon])

 :ref:`anonymize_result` contains the new :ref:`dataset`, the :ref:`risk_profile` for the new , the :ref:`dataset`,
 the anonymization status for the :ref:`dataset` and :ref:`anonymization_metrics` which contains metrics regarding the anonymzation performed on the dataset.

 ::

    # get the new dataset
    anonymized_dataset = anonymize_result.dataset
    anon_dataframe = anonymized_dataset.to_dataframe()

    # get the risk profile for the new dataset
    anon_risk_profile = anonymize_result.risk_profile

    # get the anonymiztion metrics
    anon_metrics = anonymize_result.anonymization_metrics
