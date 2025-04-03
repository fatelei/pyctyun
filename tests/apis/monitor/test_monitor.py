import os
import unittest

from pyctyun.apis.monitor.monitor import MonitorApi
from pyctyun.param.monitor import RealtimeMonitorParam


class TestMonitorApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = MonitorApi(ak=os.getenv("access_key"),
                                sk=os.getenv("secret_key"),
                                endpoint=os.getenv("endpoint"))
    
    def test_get_realtime_metric(self):
        param = RealtimeMonitorParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'deviceUUIDList': ['121.225.97.89']})
        res = self.client.get_realtime_metric(param)
        print(res)
