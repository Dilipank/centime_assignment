import requests
from config import BASE_URI, apikey
from utils.print_util import logger
from utils import handle_throttle


class RestClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = BASE_URI
        self.apikey = apikey

    def _get(self, url):
        response = requests.get(url)
        return response
        # return self.__get_responses(response)

    def _post(self, *args, **kwargs):
        pass

    def _delete(self, *args):
        pass

    @staticmethod
    def __get_responses(response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except ValueError:
            as_dict = None
        headers = response.headers
        return Response(status_code, text, as_dict, headers)


class Response:
    def __init__(self, status_code, text, _dict, headers):
        self.status_code = status_code
        self.text = text
        self.as_dict = _dict
        self.headers = headers


class APIRequest(RestClient):

    @handle_throttle
    @logger
    def get_time_series_daily(self, symbol=None, outputsize=None, datatype=None, apikey=None, no_auth=None):
        url = f'{self.base_url}&function=TIME_SERIES_DAILY&symbol={symbol}'
        if outputsize:
            url += f'&outputsize={outputsize}'
        if datatype:
            url += f'&datatype={datatype}'
        if no_auth:
            return self._get(url)
        if apikey:
            url += f'&apikey={apikey}'
        else:
            url += f'&apikey={self.apikey}'
        return self._get(url)

    def post(self, url, payload, headers):
        pass

    def delete(self, url):
        pass



