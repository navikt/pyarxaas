from uplink import Consumer, get, headers, Path, Query, post, Body, json

from python_api_consumer.models.anonymize_payload import AnonymizePayload


class AaaSConnector(Consumer):
    """ Testing AaaS restpoint connecting"""

    @json
    @post("api/anonymize")
    def anonymize_data(self, payload: Body):
        """Post data to AaaS Backend"""



