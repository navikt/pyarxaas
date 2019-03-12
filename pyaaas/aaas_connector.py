from uplink import Consumer, get, headers, Path, Query, post, Body, json


class AaaSConnector(Consumer):
    """ Testing AaaS restpoint connecting"""

    @json
    @post("api/anonymize")
    def anonymize_data(self, payload: Body):
        """Post data to AaaS Backend"""

    @json
    @post("api/analyse")
    def analyze_data(self, payload: Body):
        """Post dat to AaaS Backend"""
