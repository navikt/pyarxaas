
Introduction
============

PyARXaaS is the Python client for the ARXaaS service. You can read more about ARXaaS `here <https://github.com/oslomet-arx-as-a-service/ARXaaS>`_ .
PyARXaaS is similar to projects like  `PyGithub <https://github.com/PyGithub/PyGithub>`_. It tries to make make the itegration
of the risk analysis and de-identification functionality of ARXaaS as pain free and intuitive as possible. The main user
group of the package are data scientist that would be familiar and accustomed to work with data in Python. This user group
would prefer not to have to work in a GUI tool such as  `ARX <https://arx.deidentifier.org>`_. Instead of trying to integrate
the ARX GUI into the work flow the philosophy of the ARXaaS project has been to make a microservice component with the
de-identification functionality. And then build clients that make integration easy and seamless. The ARX project make
their core library available for use by others and this library is what the team have built on top of. ARX is the
industry leader in the de-identification space and we are grateful that the project remains open-source making projects such as this a possibility

Bellow is a coarse overview of the ARXaaS ecosystem. PyARXaaS is the first and main priority. But other clients can be developed as the need arises.

Architecture overview
---------------------

.. image:: /images/arxaas_arc.png
   :height: 300px

