.. _create_hierarchies:


Hierarchies
===========

After creating a :ref:`dataset` from some data source you can set hierarchies ARXaaS will to use when attempting to anonymize
the Dataset. ARXaaS currently only support value generalization hierarchies. Read more about different transformation
models in `ARX documentation: <https://arx.deidentifier.org/overview/transformation-models/ >`_.


Hierarchy Building
------------------
ARXaaS offer endpoints for use the ARX library hierarchy generation functionality. PyARXaaS implements abstractions to
make this process as easy as intuitive as possible.

Hierarchy generation that ARX offers falls into four different categories:

 - Redaction based hierarchies
 - Interval based hierarchies
 - Order based hierarchies
 - Date based hierarchies

ARXaaS and PyARXaaS currently only support Redaction, Interval and Order based hierarchy generation. In PyARXaaS all the
hierarchy builders are importable from the *pyaaas.hierarchy* package

----------------------------
Redaction based hierarchies
----------------------------
Redaction based hierarchies are hierarchies suited best for categorical but numeric values.
Attributes such as zipcodes are a prime canditate. The hierarchy strategy is to delete one number at the time from the
attribute column until the privacy model criteria is meet. The hierchy builder can be configured to start deleting from
either direction, but will default to RIGHT_TO_LEFT. Redaction hierarchies are the least effort hierarchy to create.

**Example**
In this example we will use a list representing a column from a hypotetical dataset. The list could be generated from any source.
Hierarchy building is works on list of data. ::

    zipcodes = [47677, 47602, 47678, 47905, 47909, 47906, 47605, 47673, 47607]

We will then import the redaction hierarchy builder class ::

    from pyaaas.hierarchy import RedactionHierarchyBuilder


