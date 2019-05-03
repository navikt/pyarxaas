.. PyAaaS documentation master file, created by
   sphinx-quickstart on Sat Feb  2 16:04:51 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: images/new_hero_2.png
   :width: 100%



Welcome to PyARXaaS's documentation!
====================================

PyARXaaS is a Python wrapper package for ARXaaS.
It provides user-friendly abstractions for the APIs exposed ARXaaS.
`Github link <https://github.com/oslomet-arx-as-a-service/PyARXaaS>`_

- For quick-start see :ref:`quick-start`
- For more in-depth information about the API see :ref:`api` .


How it works
-------------

PyARXaaS is a simple pure Python client package that provides abstractions for interacting with
a `ARXaaS <https://github.com/oslomet-arx-as-a-service/ARXaaS>`_ instance.
The package supports analyzing re-identification risks and anonymizing tabular datasets containing sensitive personal data.

Features
--------

 - :ref:`arxaas` class for configuration and calling actions.
 - :ref:`dataset`  class for encapsulating and configuring a dataset
 - :ref:`privacy_model` classes for configuring the Privacy Models to use in anonymization.
 - Easy integration with `pandas <https://pandas.pydata.org/>`_ DataFrames


Simple Use Case
---------------
Quick overview of how to get started using the package::

   # import dependencies
   from pyaaas import AaaS
   from pyaaas.privacy_models import KAnonymity
   from pyaaas import AttributeType
   from pyaaas import Dataset
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

Licensing
---------
PyARXaaS is distributed under the MIT license. See `LICENCE <https://github.com/oslomet-arx-as-a-service/PyARXaaS/blob/master/LICENSE>`_

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   user-guide/user-guide
   api/api
   notebooks/notebooks.rst




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
