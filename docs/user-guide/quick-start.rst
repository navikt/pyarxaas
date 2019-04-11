
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

Begin by importing the Dataset class and pandas which we are going to use to create a Dataset: ::

    from pyaaas.dataset import Dataset
    import pandas as pd

The we create a Dataset from a local csv file

.. note:: The dataset in this example contains the columns/fields **id, name, gender**

::

    dataframe = pd.read_csv("data.csv", sep=";")
    # create Dataset
    dataset = Dataset.from_pandas(dataframe)

*The Dataset class encapsulates the raw data, attribute types of the dataset fields and hierarchies*

Then we set the attribute type for the Dataset fields. Read more about attribute types :ref:`attribute_type` ::

    # set attribute type
    dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
    dataset.set_attribute('id', AttributeType.IDENTIFYING)


To make a call to the ARXaaS instance we need to make a instance of the AaaS class. The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally. ::

    from pyaaas.aaas import AaaS
    aaas = AaaS("http://localhost:8080")

After the AaaS object is created we can use it to call the ARXaaS instance to make a RiskProfile for our Dataset. ::

    # get the risk profle of the dataset
    risk_profile = aaas.risk_profile(dataset)



The RiskProfile object contains two properties; re-indentification risks and distributed risks. The two properties contains the different risks and the distribution of risks for the Dataset. Read more about them here: :ref:`risk_profile` ::

    # get risk metrics as a dictionary
    re_indentifiation_risk = risk_profile.re_identification_risk
    distribution_of_risk = risk_profile.distribution_of_risk

    # get risk metrivs as pandas.DataFrame
    re_i_risk_df = risk_profile.distribution_of_risk_dataframe()
    dist_risk_df = risk_profile.distribution_of_risk_dataframe()




Anonymize a dataset
-----------------------------
Anonymize a dataset using PyAaaS is also very simple.

Begin by importing the Dataset class and pandas which we are going to use to create a Dataset: ::

        from pyaaas.dataset import Dataset
        import pandas as pd


**Same as when in analyze we set the attribute type for the dataset fields**::

    # set attribute type
    dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
    dataset.set_attribute('id', AttributeType.IDENTIFYING)

**In addtion to setting attribute types we need to provide Transformation Models known as hierarchies for the attributes with type AttributeType.QUASIIDENTIFYING**
Hierarchies can be added as pandas.DataFrame objects::

    id_hierarchy = pd.read_csv("id_hierarchy.csv")
    dataset.set_hierarchy('id', id_hierarchy)

    name_hierarchy = pd.read_csv("name_hierarchy.csv")
    dataset.set_hierarchy('name', name_hierarchy)


**When anonymizing we need to supply a  :ref:`privacy_model` for ARXaaS to run on the dataset. You can read more about the models here :ref:`privacy_model` and here `ARX Privacy Models <https://arx.deidentifier.org/overview/privacy-criteria/>`_** ::

    from pyaaas.model.privacy_models import KAnonymity
    kanon = KAnonymity(4)

**To make a call to the ARXaaS instance we need to make a instance of the AaaS class. The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally.** ::

    from pyaaas.aaas import AaaS
    aaas = AaaS("http://localhost:8080")

After the AaaS object is created we can use it to call the ARXaaS instance. Back if the anonymization is succesfull we receceive an :ref:`anonymize_result` ::

    anonymize_result = aaas.anonymize(dataset, [kanon])
