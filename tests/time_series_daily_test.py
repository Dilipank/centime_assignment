import pytest
import requests

from client.time_series_daily_client import TimeSeriesDailyApi
from utils.errors import invalid_api_call_error, no_apikey_error, throttling_error
rest_obj = TimeSeriesDailyApi()


def test_throttling_failure():
    """
    Test the throttle limit of the API. Should return an error message after 5 attempts.
    """
    for _ in range(5):
        rest_obj.get_time_series_daily('IBM', throttle_ignore=False)
    response = rest_obj.get_time_series_daily('IBM', throttle_ignore=False)
    assert throttling_error.strip() == response.json()['Note']


def test_throttling_success():
    """
    Test the throttle limit of the API. Should return a valid response after waiting a minute.
    """
    for _ in range(5):
        rest_obj.get_time_series_daily('IBM')
    response = rest_obj.get_time_series_daily('IBM')
    assert len(response.json()['Time Series (Daily)']) == 100


def test_status_code_for_valid_request():
    """
    Test status code of a valid GET request.
    """
    response = rest_obj.get_time_series_daily('IBM')

    assert response.status_code == requests.codes.ok


def test_compactness_of_response():
    """
    Test the default output size of the response. Should be 100 data points.
    """
    response = rest_obj.get_time_series_daily('IBM')

    assert len(response.json()['Time Series (Daily)']) == 100


def test_full_outputsize_of_reponse():
    """
    Test full output size of the response. Should include 20+ years worth of data.
    """
    response = rest_obj.get_time_series_daily('IBM', outputsize='full')

    assert '1999-11-01' in response.json()['Time Series (Daily)'].keys()


def test_csv_datatype_of_response():
    """
    Test csv datatype of the request. Response should be in csv format.
    """
    response = rest_obj.get_time_series_daily('IBM', datatype='csv')

    with pytest.raises(Exception):
        response.json()


def test_error_message_for_unsupported_symbol():
    """
    Test the request for an unknown symbol.
    """
    response = rest_obj.get_time_series_daily('UNKNOWN')

    assert invalid_api_call_error.strip() == response.json()['Error Message']


def test_error_message_for_invalid_apikey():
    """
    Test the API when called with an invalid api key.
    """
    response = rest_obj.get_time_series_daily('IBM', apikey='InvalidApiKey')

    assert invalid_api_call_error.strip() == response.json()['Error Message']


def test_error_message_for_no_apikey():
    """
    Test the API when called without an api key.
    """
    response = rest_obj.get_time_series_daily('IBM', no_auth=True)

    assert no_apikey_error.strip() == response.json()['Error Message']







