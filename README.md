[![Build Status](https://travis-ci.com/oslomet-arx-as-a-service/PyAaaS.svg?branch=master)](https://travis-ci.com/oslomet-arx-as-a-service/PyAaaS)
[![Maintainability](https://api.codeclimate.com/v1/badges/24ea4186b037844d01ab/maintainability)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyAaaS/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24ea4186b037844d01ab/test_coverage)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyAaaS/test_coverage)
[![Documentation Status](https://readthedocs.org/projects/pyaaas/badge/?version=latest)](https://pyaaas.readthedocs.io/en/latest/?badge=latest)


# PyAaaS

Python Package for easy access to ARX Web API Service

Read more about PyAaaS at: https://pyaaas.readthedocs.io/




## Getting Started

#### Installation

````bash
pip3 install pyaaas

````

#### Basic Usage

````python
from aaas import AaaS, KAnonymity

aaas = AaaS(url) # instantiate AaaS object

aaas.set_data(df) # add data (csv_str, pandas.DataFrame)

aaas.set_attribute_types(attr) # sett attribute types for fields

aaas.set_hierarchy(field, hierarchy_data) # set a hierarchy for a field

k_anon = KAnonymity(k=4) # instantiate a PrivacyModel

aaas.set_model(k_anon) # add model


result = aaas.anonymize() # run anonymization

anonymized_df = result.to_dataframe() # retreive anonymized dataframe


````
