from uplink import Consumer, get, headers, Path, Query, post, Body

from python_api_consumer.models.anonymize_payload import AnonymizePayload


class AaaSConnector(Consumer):
    """ Testing AaaS restpoint connecting"""

    @post("api/anonymize")
    def anonymize_data(self, payload: Body):
        """Post data to AaaS Backend"""



