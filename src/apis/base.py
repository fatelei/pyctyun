from src.auth import Auth
from src.transport import Transport


class CtapiBaseClient(object):
    
    def __init__(self,
                 ak: str,
                 sk: str,
                 endpoint: str = ''):
        """Init.
        :param str ak: access key
        :param str sk: secret key
        :param str endpoint: Api hostname
        """
        self._auth = Auth(ak=ak,
                          sk=sk)
        self._transport = Transport(endpoint=endpoint)
    
    @property
    def transport(self):
        return self._transport

    def perform_request(self, api: str, params: dict, method: str = 'POST', headers=None, timeout=1):
        if method == 'POST':
            sign_headers = self.generate_sign_headers(body_params=params)
        else:
            sign_headers = self.generate_sign_headers(query_params=params)
        if headers:
            sign_headers.update(headers)
        return self._transport.perform_request(api, params=params, method=method, headers=sign_headers, timeout=timeout)
    
    def generate_sign_headers(self, query_params: dict = None, body_params: dict = None):
        return self._auth.generate_sign_headers(query_params=query_params, body_params=body_params)
