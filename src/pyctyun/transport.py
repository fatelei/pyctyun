import requests

from . import exceptions


class Transport(object):
    """Implement transport between api servers and clinet."""

    def __init__(self, endpoint):
        """Init.
        :param str endpoint: Api endpoint
        """
        self.endpoint = endpoint.rstrip('/')

    def perform_request(self, api, params: dict, method='GET', headers=None, timeout=1):
        url = f'{self.endpoint}{api}'

        try:
            if method == 'POST':
                resp = requests.post(url, json=params, headers=headers)
            else:
                resp = requests.get(url, params=params, headers=headers, json={})
            return resp.json()
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout) as e:
            raise exceptions.TimeoutError(
                status_code=504, reason=str(e))
