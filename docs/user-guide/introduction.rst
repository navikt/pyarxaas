
Introduction
============

PyARXaaS is the Python client for the ARXaaS service. You can read more about ARXaaS `here <https://github.com/oslomet-arx-as-a-service/ARXaaS>`_ .
PyARXaaS is similar to projects like  `PyGithub <https://github.com/PyGithub/PyGithub>`_. It tries to make make the integration
of the risk analysis and de-identification functionality of ARXaaS as easy and intuitive as possible. The main user
group of the package are data scientist that would be familiar and accustomed to work with data in Python. This user group
would prefer not to have to work in a GUI tool such as  `ARX <https://arx.deidentifier.org>`_. The philosophy of the ARXaaS project has been to make a microservice component with the
de-identification functionality, and building clients that make integration easy and seamless, instead of trying to integrate the ARX GUI into the work flow.

The ARX project makes their core library available by making it open source, and this library is what the team have used as the building foundation for the service. ARX is the
industry leader in the de-identification space, and the team is grateful that the project remains open source, making projects such as this possible.

Bellow is a coarse overview of the ARXaaS ecosystem. PyARXaaS is the first and main client priority. But other clients can be developed as the need arises.

Architecture overview
---------------------

.. image:: /images/arxaas_arc.png
   :height: 300px

