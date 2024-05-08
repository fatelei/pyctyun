import base64
import datetime
import hashlib
import hmac
import json
import uuid
from collections import OrderedDict
from urllib.parse import urlencode


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
    
    def b64encode_hmac_sha256(self, key, value):
        if isinstance(key, str):
            key = bytearray(key, 'utf8')
        
        if isinstance(value, str):
            value = bytearray(value, 'utf8')
        return base64.b64encode(hmac.new(key, value, hashlib.sha256).digest()).decode('utf8')
    
    def hmac_sha256(self, key, value):
        if isinstance(key, str):
            key = bytearray(key, 'utf8')
        
        if isinstance(value, str):
            value = bytearray(value, 'utf8')
        return hmac.new(key, value, hashlib.sha256).digest()
    
    def _build_signature(self, query_params, body_params, eop_date, request_uuid):
        # body_str = json.dumps(body_params) if body_params else ''
        body_str = json.dumps(body_params)
        body_digest = hashlib.sha256(body_str.encode('utf-8')).hexdigest()
        # 请求头中必要的两个参数
        header_str = f'ctyun-eop-request-id:{request_uuid}\neop-date:{eop_date}\n'
        # url中的参数，或get参数
        
        keys = sorted(query_params.keys())
        query_dict = OrderedDict()
        for key in keys:
            query_dict[key] = query_params[key]
        
        query_str = urlencode(query_dict)
        
        signature_str = f'{header_str}\n{query_str}\n{body_digest}'
        
        sign_date = eop_date.split('T')[0]
        
        # 计算鉴权密钥
        k_time = self.hmac_sha256(self.sk, eop_date)
        k_ak = self.hmac_sha256(k_time, self.ak)
        k_date = self.hmac_sha256(k_ak, sign_date)
        signature_base64 = self.b64encode_hmac_sha256(k_date, signature_str)
        # 构建请求头的鉴权字段值
        sign_header = f'{self.ak} Headers=ctyun-eop-request-id;eop-date Signature={signature_base64}'
        return sign_header
    
    def generate_sign_headers(self, query_params: dict = None, body_params: dict = None) -> dict:
        query_params = query_params or {}
        body_params = body_params or {}
        
        now = datetime.datetime.now()
        eop_date = now.strftime("%Y%m%dT%H%M%SZ")
        request_uuid = str(uuid.uuid1())
        authorization = self._build_signature(query_params=query_params, body_params=body_params,
                                              eop_date=eop_date,
                                              request_uuid=request_uuid)
        headers = {
            'eop-date': eop_date,
            'ctyun-eop-request-id': request_uuid,
            'Eop-Authorization': authorization
        }
        return headers
