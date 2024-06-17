import os
import unittest

from src.apis.monitor.monitor_item import MonitorItemApi
from src.param.montior_item import MonitorItemParam


class TestMonitorItemApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = MonitorItemApi(ak=os.getenv("access_key"),
                                    sk=os.getenv("secret_key"),
                                    endpoint=os.getenv("endpoint"))
    
    def test_get_monitor_items(self):
        param = MonitorItemParam(**{'deviceType': 'eip'})
        res = self.client.get_monitor_items(param)
        print(res)
