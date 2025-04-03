import os
import unittest

from pyctyun.apis.monitor.monitor_item import MonitorItemApi
from pyctyun.param.montior_item import MonitorItemParam


class TestMonitorItemApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = MonitorItemApi(ak=os.getenv("access_key"),
                                    sk=os.getenv("secret_key"),
                                    endpoint=os.getenv("endpoint"))
    
    def test_get_monitor_items(self):
        param = MonitorItemParam(**{'regionID': 'bb9fdb42056f11eda1610242ac110002'})
        res = self.client.get_monitor_items(param)
        print(res)
