.. PyAaaS documentation master file, created by
   sphinx-quickstart on Sat Feb  2 16:04:51 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyAaaS's documentation!
==================================

PyAaaS is a Python wrapper package for ARXaaS.
It provides user-friendly abstractions for the APIs exposed ARXaaS.
`Github link <https://github.com/oslomet-arx-as-a-service/PyAaaS>`_

For more in-depth information about the API see :ref:`api` .

Simple use
----------
Quick overview of how to get started using the package::


   # import dependencies
   from pyaaas.aaas import AaaS
   from pyaaas.models.privacy_models import KAnonymity
   from pyaaas.attribute_type import AttributeType
   from pyaaas.dataset import Dataset
   import pandas as pd

   aaas = AaaS(url) # url contains url to AaaS web service

   df = pd.read_csv("data.csv", sep=";")

   # create Dataset
   dataset = Dataset.from_pandas(data_df)


   # set attribute type
   dataset.set_attributes(['name','gender'], AttributeType.QUASIIDENTIFYING)
   dataset.set_attribute('id', AttributeType.IDENTIFYING)

   # get the risk profle of the dataset
   risk_profile = aaas.risk_profile(dataset)

   # get risk metrics
   re_indentifiation_risk = risk_profile.re_identification_risk
   distribution_of_risk = risk_profile.distribution_of_risk


How it works
------------

PyAaaS is a simple pure Python package that only provides abstractions for interacting with the ARXaaS Web Service.
The ARXaaS Web Service uses the ARX library to analyze and anonymize the dataset.

Features
--------

 - AaaS class for configuration and calling actions.
 - Dataset class for encapsulating and configuring a dataset
 - PrivacyModel classes for configurating the Privacy Models to use.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   user-guide/user-guide
   api/api




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
