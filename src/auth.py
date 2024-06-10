import base64
import datetime
import hashlib
import hmac
import json
import uuid

from urllib.parse import quote


class Auth(object):
    """Get access token by crop id and secret."""

    def __init__(self, ak: str, sk: str):
        """Init.
        :param str app_key: App key
        :param str app_secret: App secret
        :param str sign_method:
        :param str endpoint:
        """
        self.ak = ak
        self.sk = sk

    def hmac_sha256(self, secret, data):
        if isinstance(secret, str):
            secret = secret.encode('utf8')
        if isinstance(data, str):
            data = data.encode('utf8')
        return hmac.new(secret, data, digestmod=hashlib.sha256).digest()

    def base64_of_hmac(self, data):
        return base64.b64encode(data).decode('utf8')

    def get_request_uuid(self):
        return str(uuid.uuid1())

    def get_sorted_str(self, data):
        sorted_data = sorted(data.items(), key=lambda item: item[0])
        # str_list = map(lambda (x, y): '%s=%s' % (x, y), sorted_data)
        str_list = map(lambda x: '%s=%s' %
                       (x[0], quote(str(x[1]))), sorted_data)
        return '&'.join(str_list)

    def build_sign(self, query_params, body_params, eop_date, request_uuid):
        body_str = json.dumps(body_params)
        body_digest = hashlib.sha256(body_str.encode('utf-8')).hexdigest()
        # 请求头中必要的两个参数
        header_str = 'ctyun-eop-request-id:%s\neop-date:%s\n' % (
            request_uuid, eop_date)
        # url中的参数，或get参数
        query_str = self.get_sorted_str(query_params)

        signature_str = '%s\n%s\n%s' % (header_str, query_str, body_digest)
        # sys.stdout.write(repr('signature_str is: %s' % signature_str))
        sign_date = eop_date.split('T')[0]

        # 计算鉴权密钥
        k_time = self.hmac_sha256(self.sk, eop_date)
        k_ak = self.hmac_sha256(k_time, self.ak)
        k_date = self.hmac_sha256(k_ak, sign_date)

        signature_base64 = self.base64_of_hmac(
            self.hmac_sha256(k_date, signature_str))
        # 构建请求头的鉴权字段值
        sign_header = '%s Headers=ctyun-eop-request-id;eop-date Signature=%s' % (
            self.ak, signature_base64)
        return sign_header

    def generate_sign_headers(self,
                              query_params: dict = None,
                              body_params: dict = None) -> dict:
        query_params = query_params or {}
        body_params = body_params or {}

        now = datetime.datetime.now()
        eop_date = now.strftime("%Y%m%dT%H%M%SZ")
        request_uuid = self.get_request_uuid()
        authorization = self.build_sign(query_params=query_params,
                                        body_params=body_params,
                                        eop_date=eop_date,
                                        request_uuid=request_uuid)
        headers = {
            'eop-date': eop_date,
            'ctyun-eop-request-id': request_uuid,
            'Eop-Authorization': authorization,
        }
        return headers
