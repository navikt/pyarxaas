.. _attribute_type:

Attribute Type
=================

1. Identifying attributes are associated with a high risk of re-identification. They will be removed from the dataset. Typical examples are names or Social Security Numbers.

2. Quasi-identifying attributes can in combination be used for re-identification attacks. They will be transformed. Typical examples are gender, date of birth and ZIP codes.

3. Sensitive attributes encode properties with which individuals are not willing to be linked with. As such, they might be of interest to an attacker and, if disclosed, could cause harm to data subjects. They will be kept unmodified but may be subject to further constraints, such as t-closeness or l-diversity. Typical examples are diagnoses.

4. Insensitive attributes are not associated with privacy risks. They will be kept unmodified.


AttributeType respresents data regarding the identification implication for a filed in a dataset

.. module:: pyarxaas.models.attribute_type

.. autoclass:: AttributeType
    :members:
