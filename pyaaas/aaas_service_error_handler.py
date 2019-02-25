import requests


def is_response_error(response: requests.Response):
    return response.status_code == 200 # NOTE: Will return false on other valid status codes like 201
