from utils.rest_operations import RestClient
from utils import handle_throttle
from utils.print_util import logger


class TimeSeriesDailyApi(RestClient):

    @handle_throttle
    @logger
    def get_time_series_daily(self, symbol=None, outputsize=None, datatype=None, apikey=None, no_auth=None,
                              throttle_ignore=True):
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