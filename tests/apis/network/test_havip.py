import os
import unittest

from pyctyun.apis.network.havip import HavipApi
from pyctyun.param.havip import BindOrUnbindVipParam, ListVipParam


class TestHavipApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = HavipApi(ak=os.getenv("access_key"),
                              sk=os.getenv("secret_key"),
                              endpoint=os.getenv("endpoint"))
        

    @unittest.skip
    def test_bind(self):
        param = BindOrUnbindVipParam(**{
            "clientToken": "xxxxxxxxx",
            "regionID": "bb9fdb42056f11eda1610242ac110002",
            "resourceType": "VM",
            "haVipID": "xxx",
            "instanceID": "xxx",
            "networkInterfaceID": "xx"
        })
        resp = self.client.bind_havip(param)
        self.assertEqual(800, resp.status_code)
    
    def test_list_vip(self):
        param = ListVipParam(**{
            "regionID": "bb9fdb42056f11eda1610242ac110002",
            "clientToken": "ssss"
        })
        
        resp = self.client.list_havip(param)
        self.assertEqual(800, resp.status_code)
        self.assertEqual(16, len(resp.return_obj))
