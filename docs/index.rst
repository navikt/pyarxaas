.. PyAaaS documentation master file, created by
   sphinx-quickstart on Sat Feb  2 16:04:51 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyAaaS's documentation!
==================================

PyAaaS is a Python wrapper package for the AaaS Web Service.
It provides user-friendly abstractions for the APIs exposed by the AaaS Web Service.

Simple use
----------
Quick overview of how to get started using the package::

   from pyaaas import AaaS
   aaas = AaaS(url) # url contains url to AaaS web service

   ... # add data and configurations

   result = aaas.anonymize()
   df = result.to_dataframe()

This will use the provided Privacy Models and Transform Models to attempt to anonymize the dataset with minimal information loss.

How it works
------------

PyAaaS is a simple pure Python package that only provides abstractions for interacting with the AaaS Web Service.
The AaaS Web Service uses the ARX library to analyze and anonymize the dataset.

Features
--------

 - AaaS class for configuration and calling actions
 - PrivacyModel classes for configurating the Privacy Models to use
 - HirarchyGenerator classes for easy generation of Transform Model hierarchies.



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
