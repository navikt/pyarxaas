[![Build Status](https://travis-ci.com/oslomet-arx-as-a-service/PyARXaaS.svg?branch=master)](https://travis-ci.com/oslomet-arx-as-a-service/PyARXaaS)
[![Maintainability](https://api.codeclimate.com/v1/badges/a894c7aae5e86e694ad4/maintainability)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyARXaaS/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a894c7aae5e86e694ad4/test_coverage)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyARXaaS/test_coverage)
[![Documentation Status](https://readthedocs.org/projects/pyaaas/badge/?version=latest)](https://pyaaas.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# PyARXaaS

Python Package for interfacing with ARXaaS in Python

Read more about PyARXaaS at: https://pyaaas.readthedocs.io/


## Getting Started

#### Installation

````bash
pip install pyarxaas

````

#### Basic Usage

````python

   # import dependencies
   from pyarxaas import ARXaaS
   from pyarxaas.privacy_models import KAnonymity
   from pyarxaas import AttributeType
   from pyarxaas import Dataset
   import pandas as pd

   arxaas = ARXaaS(url) # url contains url to AaaS web service

   df = pd.read_csv("data.csv")

   # create Dataset
   dataset = Dataset.from_pandas(df)


   # set attribute type
   dataset.set_attributes(AttributeType.QUASIIDENTIFYING, 'name', 'gender')
   dataset.set_attribute(AttributeType.IDENTIFYING, 'id')

   # get the risk profle of the dataset
   risk_profile = arxaas.risk_profile(dataset)

   # get risk metrics
   re_indentifiation_risk = risk_profile.re_identification_risk
   distribution_of_risk = risk_profile.distribution_of_risk
````
