.. _connect_to_arxaas:


Connecting to and using ARXaaS
===============================

Calls to `ARXaaS <https://github.com/oslomet-arx-as-a-service/ARXaaS>`_ is made through the :ref:`arxaas` class.
ARXaaS implements methods for the following functionality:

- Anonymize a :ref:`dataset` object
- Analyze re-identification risk for a :ref:`dataset` object
- Create generalization hierarchies (See: :ref:`create_hierarchies`)


Creating
----------
When creating a instance of the ARXaaS class you need to pass a full url to the service running.

Example ::

    from pyarxaas import ARXaaS    
    arxaas = ARXaaS(https://localhost:8080)


Risk Profile
-------------
Re-identfification risk for prosecutor, journalist and markteter attack models can be obtained using the ARXaaS
risk_profile method. The method takes a :ref:`dataset` object and returns a :ref:`risk_profile`.
See :ref:`using_dataset` for more on the Dataset class. More in depth information on re-identificaiton risk `ARX | risk analysis <https://arx.deidentifier.org/anonymization-tool/risk-analysis>`_

Example ::

    risk_profile = arxaas.risk_profile(dataset)


Risk profile contains different properties containg analytics on the dataset re-identification risk.
Most important is the re-identification risk property. ::

    # create risk profile ...
    risks = risk_profile.re_identification_risk

The property contains a mapping of risk => value. What is a acceptable risk depends entirely on the context of the dataset.

Anonymization
--------------
Anonymizing a dataset is as simple as passing a :ref:`dataset` containing the neccessary hierarchies, a sequence of
:ref:`privacy_model` to use and optionally a suppersion limit to the anonymize() method. The method, if succesfull returns
a :ref:`anonymize_result` object containing the new dataset.

Example ::

    kanon = KAnonymity(2)
    ldiv = LDiversityDistinct(2, "disease") # in this example the dataset has a disease field
    anonymize_result = arxaas.anonymize(dataset, [kanon, ldiv], 0.2)
    anonymized_dataset = anonymize_result.dataset


Hierarchy Generation
---------------------
Generalizaiton hierarchies are a important part of anonymization. ARXaaS contains a hierarchy() method. It takes a configured
:ref:`hierarchy_builders` object and a dataset column represented as a common Python list. It returns a 2D list structure
containing a new hierarchy.

Example making a redaction hierarchy ::

    redaction_builder = RedactionHierarchyBuilder()
    zipcodes = [47677, 47602, 47678, 47905, 47909, 47906, 47605, 47673, 47607]
    zipcode_hierarchy = arxaas.hiearchy(redaction_builder, zipcodes)
