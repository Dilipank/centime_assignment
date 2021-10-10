import requests
from config import BASE_URI, apikey


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

    def _post(self, *args, **kwargs):
        pass

    def _delete(self, *args):
        pass





