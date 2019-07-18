.. _risk_profile:

RiskProfile
=================

RiskProfile encapsulates the re-identification risks associated with a given Dataset

RiskProfile contains two main properties
----------------------------------------
**Re-Identification Risks**

- Lowest prosecutor re-identification risk.
- Individuals affected by lowest risk.
- Highest prosecutor re-identification risk.
- Individuals affected by highest risk.
- Average prosecutor re-identification risk.
- Fraction of unique records.
- Attacker success rate against the re-identification risk.
- Population Model name
- Quasi-identifiers

**Distribution of Risks**

The distribution of re-identification risks amongst the records of the dataset

.. module:: pyarxaas.models.risk_profile

.. autoclass:: RiskProfile
    :members:
