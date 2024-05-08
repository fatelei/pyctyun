import json
import logging
import time
import urllib.request
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError

from src import exceptions


class Transport(object):
    """Implement transport between api servers and clinet."""

    def __init__(self, endpoint):
        """Init.
        :param str endpoint: Api endpoint
        """
        self.endpoint = endpoint.rstrip('/')

    def perform_request(self, api, params: dict, method='GET', headers=None, timeout=1):
        url = f'{self.endpoint}{api}'
        
        if method == 'POST':
            req = urllib.request.Request(url, method=method)
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            jsondata = json.dumps(params)
            data = jsondata.encode('utf-8')  # needs to be bytes
            req.add_header('Content-Length', str(len(data)))
        else:
            query_str = urlencode(params)
            url = f'{url}?{query_str}'
            req = urllib.request.Request(url, method=method)
            data = None
            
        if headers:
            for k, v in headers.items():
                req.add_header(k, v)
            
        try:
            s = time.time()
            with urllib.request.urlopen(req, data=data, timeout=timeout) as response:
                raw_data = response.read()
                elapse = time.time() - s
                logging.info(f"response from ctapi {url} {method} {response.status}")
                if 400 <= response.status < 500:
                    raise exceptions.ClientRequestError(status_code=response.status, reason=raw_data.decode('utf8'))
                elif response.status >= 500:
                    raise exceptions.InternalServerError(status_code=response.status, reason=raw_data.decode('utf8'))
                return json.loads(raw_data)
        except json.JSONDecodeError as e:
            logging.warning(e, exc_info=True)
            raise exceptions.CtapiException(status_code=500, reason='unexcept json')
        except HTTPError as e:
            logging.warning(e, exc_info=True)
            raise exceptions.CtapiException(status_code=e.code, reason=e.reason)
        except URLError as e:
            logging.warning(e, exc_info=True)
            raise exceptions.CtapiException(status_code=500, reason=e.reason)
        except TimeoutError as e:
            logging.warning(e, exc_info=True)
            raise exceptions.TimeoutError(status_code=504, reason='timeout')
