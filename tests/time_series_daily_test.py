import requests

from utils.rest_operations import APIRequest
from utils.errors import unsupported_symbol_error, no_apikey_error
from utils.print_util import log_request_response
rest_obj = APIRequest()


def test_status_code_for_valid_request():
    """

    """
    response = rest_obj.get_time_series_daily('IBM')
    # log_request_response(response)
    assert response.status_code == requests.codes.ok



def test_compactness_of_response():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('IBM')

    assert len(response.json()['Time Series (Daily)']) == 100

def test_full_outputsize_of_reponse():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('IBM', outputsize='full')

    assert '1999-11-01' in response.json()['Time Series (Daily)'].keys()

def test_datatype_of_response():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('IBM', datatype='csv')

    assert response.json() is None

def test_error_message_for_unsupported_symbol():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('UNKNOWN')

    assert unsupported_symbol_error.strip() == response.json()['Error Message']

def test_error_message_for_invalid_apikey():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('IBM', apikey='InvalidApiKey')

    assert unsupported_symbol_error.strip() == response.json()['Error Message']

def test_error_message_for_no_apikey():
    """

    :return:
    """
    response = rest_obj.get_time_series_daily('IBM', no_auth=True)

    assert no_apikey_error.strip() == response.json()['Error Message']

