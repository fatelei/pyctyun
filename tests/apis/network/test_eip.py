import os
import unittest

from pyctyun.apis.network.eip import EipApi
from pyctyun.param.eip import ListEipParam


class TestEipApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = EipApi(ak=os.getenv("access_key"),
                            sk=os.getenv("secret_key"),
                            endpoint=os.getenv("endpoint"))
    
    def test_list_eip(self):
        resp = self.client.list_eip(ListEipParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'clientToken': 'xxx',
            "pageNo": 1,
            "pageSize": 1
        }))
        self.assertEqual(800, resp.status_code)
        data = resp.return_obj.model_dump(by_alias=True)
        self.assertIn('eips', data)
        self.assertEqual(1, resp.current_count)
        
        for eip in data['eips']:
            self.assertIn('ID', eip)
            self.assertIn('name', eip)
            self.assertIn('eipAddress', eip)
            self.assertIn('associationID', eip)
            self.assertIn('associationType', eip)
            self.assertIn('privateIpAddress', eip)
            self.assertIn('bandwidth', eip)
            self.assertIn('bandwidthID', eip)
            self.assertIn('bandwidthType', eip)
            self.assertIn('status', eip)
            self.assertIn('tags', eip)
            self.assertIn("createdAt", eip)
            self.assertIn("updatedAt", eip)
            self.assertIn("expiredAt", eip)
    
    def test_new_list_eip(self):
        resp = self.client.new_list_eip(ListEipParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'clientToken': 'xxx',
            'pageNumber': 2,
            'pageSize': 2
        }))
        self.assertEqual(800, resp.status_code)
        data = resp.return_obj.model_dump(by_alias=True)
        # print(data)
        self.assertIn('eips', data)
        self.assertIn("currentCount", data)
        self.assertIn("totalPage", data)
        self.assertIn("totalCount", data)
        self.assertEqual(2, resp.return_obj.current_count)

        for eip in data['eips']:
            self.assertIn('ID', eip)
            self.assertIn('name', eip)
            self.assertIn('eipAddress', eip)
            self.assertIn('associationID', eip)
            self.assertIn('associationType', eip)
            self.assertIn('privateIpAddress', eip)
            self.assertIn('bandwidth', eip)
            self.assertIn('bandwidthID', eip)
            self.assertIn('bandwidthType', eip)
            self.assertIn('status', eip)
            self.assertIn('tags', eip)
            self.assertIn("createdAt", eip)
            self.assertIn("updatedAt", eip)
            self.assertIn("expiredAt", eip)
