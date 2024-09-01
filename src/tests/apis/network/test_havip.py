import os
import unittest

from src.apis.network.havip import HavipApi
from src.param.havip import BindOrUnbindVipParam


class TestHavipApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = HavipApi(ak=os.getenv("access_key"),
                              sk=os.getenv("secret_key"),
                              endpoint=os.getenv("endpoint"))
        

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
