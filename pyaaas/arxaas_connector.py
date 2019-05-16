from uplink import Consumer, get, headers, Path, Query, post, Body, json
import logging

from uplink import response_handler
from requests.exceptions import RequestException, HTTPError


@response_handler
def raise_for_status(response):
    """
    Raises exceptions for not successful response status codes
    :param response: response from service
    :return:
    """
    if 400 <= response.status_code < 500:
        raise RequestException(response.text)
    if response.status_code >= 500:
        raise HTTPError(response.text)
    return response


class ARXaaSConnector(Consumer):
    """ Understands connection to ARXaaS endpoints"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger(__name__)

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
        try:
            response = self.root()
            logger.info(f"Connected to url={url} status={response.status_code}")
        except Exception as err:
            logger.warning(f"Cannot connect to url={url} message={err}")

