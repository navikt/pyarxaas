[![Build Status](https://travis-ci.com/oslomet-arx-as-a-service/PyAaaS.svg?branch=master)](https://travis-ci.com/oslomet-arx-as-a-service/PyAaaS)
[![Maintainability](https://api.codeclimate.com/v1/badges/a894c7aae5e86e694ad4/maintainability)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyARXaaS/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a894c7aae5e86e694ad4/test_coverage)](https://codeclimate.com/github/oslomet-arx-as-a-service/PyARXaaS/test_coverage)
[![Documentation Status](https://readthedocs.org/projects/pyaaas/badge/?version=latest)](https://pyaaas.readthedocs.io/en/latest/?badge=latest)


# PyAaaS

Python Package for easy access to ARX Web API Service

Read more about PyAaaS at: https://pyaaas.readthedocs.io/




## Getting Started

#### Installation

````bash
pip install pyaaas

````

#### Basic Usage

````python

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

````
