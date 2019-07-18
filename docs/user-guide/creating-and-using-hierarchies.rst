.. _create_hierarchies:


Creating Hierarchies
====================

After creating a :ref:`dataset` from some data source, you can set the hierarchies ARXaaS will use when attempting to anonymize
the Dataset. ARXaaS currently only support value generalization hierarchies. Read more about different transformation
models in `ARX documentation <https://arx.deidentifier.org/overview/transformation-models>`_.

Hierarchy Building
------------------
ARXaaS offers an endpoint to use the ARX library hierarchy generation functionality. PyARXaaS implements abstractions to
make this process as easy and intuitive as possible.

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
Attributes such as zipcodes are a prime candidate. The hierarchy strategy is to delete one number at a time from the
attribute column until the privacy model criteria is meet. The hierarchy builder can be configured to start deleting from
either direction, but will default to RIGHT_TO_LEFT. Redaction based hierarchies are the hierarchies with the least effort to create.

**Example**
In this example we will use a list of zipcodes representing a column from a hypothetical dataset. The list could be generated from any source.
Hierarchy building works on list of strings or numbers. ::

    zipcodes = [47677, 47602, 47678, 47905, 47909, 47906, 47605, 47673, 47607]

We will then import the redaction hierarchy builder class ::

    from pyarxaas.hierarchy import RedactionHierarchyBuilder

The :ref:`redaction_hierarchy_builder` class is a simple class and all configuration is optional. When instantiating the
class the user can pass in parameters to configure how the resulting hierarchy should be built. See :ref:`redaction_hierarchy_builder` for more on the parameters.

**Creating a simple redaction hierarchy** ::

    redaction_builder = RedactionHierarchyBuilder() # Create builder

The builder defines a template to build the resulting hierarchy from. Now that we have the list to create a hierarchy for
and a builder to build it with can call ARXaaS to make the hierarchy. ::

    from pyarxaas import ARXaaS
    # establishing a connection to the ARXaaS service using a url, in this case ARXaaS is running locally on port 8080
    arxaas = ARXaaS("http://localhost:8080")

With the connection to ARXaaS established we can create the hierarchy. ::

    redaction_hierarchy = arxaas.hierarchy(redaction_based, zipcodes) # pass builder and column to arxaas

The resulting hierarchy looks like this: ::

    [['47677', '4767*', '476**', '47***', '4****', '*****'],
    ['47602', '4760*', '476**', '47***', '4****', '*****'],
    ['47678', '4767*', '476**', '47***', '4****', '*****'],
    ['47905', '4790*', '479**', '47***', '4****', '*****'],
    ['47909', '4790*', '479**', '47***', '4****', '*****'],
    ['47906', '4790*', '479**', '47***', '4****', '*****'],
    ['47605', '4760*', '476**', '47***', '4****', '*****'],
    ['47673', '4767*', '476**', '47***', '4****', '*****'],
    ['47607', '4760*', '476**', '47***', '4****', '*****']]

---------------------------
Interval based hierarchies
---------------------------
Interval based hierarchies are well suited for continuous numeric values. Attributes such as age, income or credit score
are typically generalized with a interval based hierarchy. The Interval based hierarchy builder requires the user to specify intervals
in which to generalize values in the attribute. Optionally these intervals can be labeled. In addition intervals
can be grouped upwards using levels and groups to create a deeper hierarchy.

**Example**
In this example we will use a list of ages representing a column from a hypothetical dataset. ::

    ages = [29, 22, 27, 43, 52, 47, 30, 36, 32]

We import the :ref:`interval_hierarchy_builder` class from the hierarchy package. ::

    from pyarxaas.hierarchy import IntervalHierarchyBuilder

Then we instantiate the builder. :ref:`interval_hierarchy_builder` takes no constructor arguments. ::

    interval_based = IntervalHierarchyBuilder()

Add intervals to the builder. The intervals must be continuous(without gaps) ::

    interval_based.add_interval(0,18, "child")
    interval_based.add_interval(18,30, "young-adult")
    interval_based.add_interval(30,60, "adult")
    interval_based.add_interval(60,120, "old")

(Optionally) Add groupings. Groupings are added to a specific level and are order based according to the interval order. ::

    interval_based.level(0)\
        .add_group(2, "young")\
        .add_group(2, "adult")

Call the ARXaaS service to create the hierarchy ::

    interval_hierarchy = arxaas.hierarchy(interval_based, ages)

The hierarchy looks like this: ::

    [['29', 'young-adult', 'young', '*'],
     ['22', 'young-adult', 'young', '*'],
     ['27', 'young-adult', 'young', '*'],
     ['43', 'adult', 'adult', '*'],
     ['52', 'adult', 'adult', '*'],
     ['47', 'adult', 'adult', '*'],
     ['30', 'adult', 'adult', '*'],
     ['36', 'adult', 'adult', '*'],
     ['32', 'adult', 'adult', '*']]

----------------------
Order based hierarchy
----------------------
:ref:`order_hierarchy_builder` are suited for categorical attributes. Attributes such as country, education level and
employment status.

Order based hierarchies are built using groupings with optional labeling. This means that grouping is completed on the
list of values as it is. This means the list has to be sorted according to some ordering before a hierarchy can be made.
On the positive side. Order based hierarchies are usually very reusable depending on the domain.

In this example we will use a column of diseases. ::

    diseases = ['bronchitis',
                'flu',
                'gastric ulcer',
                'gastritis',
                'pneumonia',
                'stomach cancer']

In this case we will sort the diseases according to the disease location; *lung-disease* or *stomach-disease*. But this
sorting can be as sophistical as the user wants. ::

    unique_diseases[2], unique_diseases[4] = unique_diseases[4], unique_diseases[2]
    unique_diseases

    #['bronchitis',
    # 'flu',
    # 'pneumonia',
    # 'gastritis',
    # 'gastric ulcer',
    # 'stomach cancer']


Import :ref:`order_hierarchy_builder` ::

    from pyarxaas.hierarchy import OrderHierarchyBuilder

Create instance to use. ::

    order_based = OrderHierarchyBuilder()

Group the values.
Note that the groups are applied to the values as they are ordered in the list. Adding labels are optional, if labels
are not set the resulting field will be a concatenation of the values included in the group. ::

    order_based.level(0)\
        .add_group(3, "lung-related")\
        .add_group(3, "stomach-related")

Call the ARXaaS service to create the hierarchy ::

    order_hierarchy = arxaas.hierarchy(order_based, diseases)

The resulting hierarchy looks like this: ::

    [['bronchitis', 'lung-related', '*'],
     ['flu', 'lung-related', '*'],
     ['pneumonia', 'lung-related', '*'],
     ['gastritis', 'stomach-related', '*'],
     ['gastric ulcer', 'stomach-related', '*'],
     ['stomach cancer', 'stomach-related', '*']]

----------------------
Date based hierarchy
----------------------

:ref:`date_hierarchy_builder` are suited for date and timestamp attributes. The date values must be formated according to Java
SimpleDateFormat `Link to SimpleDateFormat documentation  <https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html>`_.

In this example we will use a column of timestamps. ::

      timestamps = ["2020-07-16 15:28:024",
         "2019-07-16 16:38:025",
         "2019-07-16 17:48:025",
         "2019-07-16 18:48:025",
         "2019-06-16 19:48:025",
         "2019-06-16 20:48:025"]


Import :ref:`date_hierarchy_builder`. ::

       from pyarxaas.hierarchy import DateHierarchyBuilder

Create instance to use. ::

    date_based = DateHierarchyBuilder("yyyy-MM-dd HH:mm:SSS",
                          DateHierarchyBuilder.Granularity.SECOND_MINUTE_HOUR_DAY_MONTH_YEAR,
                          DateHierarchyBuilder.Granularity.MINUTE_HOUR_DAY_MONTH_YEAR,
                          DateHierarchyBuilder.Granularity.YEAR)


Call the ARXaaS service to create the hierarchy ::

    timestamp_hierarchy = arxaas.hierarchy(date_based, timestamps)

The resulting hierarchy looks like this: ::

    [['2020-07-16 15:28:024', '16.07.2020-15:28:00', '16.07.2020-15:28', '2020'],
     ['2019-07-16 16:38:025', '16.07.2019-16:38:00', '16.07.2019-16:38', '2019'],
     ['2019-07-16 17:48:025', '16.07.2019-17:48:00', '16.07.2019-17:48', '2019'],
     ['2019-07-16 18:48:025', '16.07.2019-18:48:00', '16.07.2019-18:48', '2019'],
     ['2019-06-16 19:48:025', '16.06.2019-19:48:00', '16.06.2019-19:48', '2019'],
     ['2019-06-16 20:48:025', '16.06.2019-20:48:00', '16.06.2019-20:48', '2019']]
