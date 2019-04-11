
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

Then we set the attribute type for the Dataset fields. Read more about attribute types :ref:`_attribute-type` ::

    # set attribute type
    dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
    dataset.set_attribute('id', AttributeType.IDENTIFYING)


To make a call to the ARXaaS instance we need to make a instance of the AaaS class. The AaaS connector class needs a url to the ARXaaS instance. In this example we have ARXaaS running locally. ::

    from pyaaas.aaas import AaaS
    aaas = AaaS(http://localhost:8080)

After the AaaS object is created we can use it to call the ARXaaS instance to make a RiskProfile for our Dataset. ::

    # get the risk profle of the dataset
    risk_profile = aaas.risk_profile(dataset)



