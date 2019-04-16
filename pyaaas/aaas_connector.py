from uplink import Consumer, get, headers, Path, Query, post, Body, json
import logging

from uplink import response_handler
from urllib3.util import parse_url
from requests.exceptions import RequestException, HTTPError


@response_handler
def raise_for_status(response):
    if 400 <= response.status_code < 500:
        raise RequestException(response.text)
    if response.status_code >= 500:
        raise HTTPError(response.text)
    return response


class AaaSConnector(Consumer):
    """ Testing AaaS restpoint connecting"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger(__file__)

    @raise_for_status
    @json
    @post("api/anonymize")
    def anonymize_data(self, payload: Body):
        """Post data to AaaS Backend"""

    @raise_for_status
    @json
    @post("api/analyze")
    def risk_profile(self, payload: Body):
        """Post data to AaaS Backend"""

    @raise_for_status
    @json
    @post("api/hierarchy")
    def hierarchy(self, payload: Body):
        """Post data to AaaS Backend"""

    @raise_for_status
    @get("/")
    def root(self):
        """ Get root of service """

    def test_connection(self):
        url = self.session.base_url
        logger = self._logger
        parsed_url = parse_url(url)
        try:
            response = self.root()
            port = 80
            if parsed_url.port:
                port = parsed_url.port
            logger.info(f"Connected to url={parsed_url.host}, port={port} status={response.status_code}")
        except Exception as err:
            logger.warning(f"FAILED connecting to url={parsed_url.host} on port={parsed_url.port} message={err}")

