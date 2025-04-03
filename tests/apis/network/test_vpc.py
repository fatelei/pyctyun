import os
import unittest

from pyctyun.apis.network.vpc import VpcApi
from pyctyun.param.vpc import ListVPCParam, ShowVPCParam, UpdateVPCParam, CreateVPCParam, UpdateVPCIPv6StatusParam, \
    DeleteVPCParam


class TestVpcApi(unittest.TestCase):
    client = None
    vpc_id = None
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = VpcApi(ak=os.getenv("access_key"),
                            sk=os.getenv("secret_key"),
                            endpoint=os.getenv("endpoint"))
        
        resp = cls.client.create_vpc(CreateVPCParam(**{
            "regionID": "bb9fdb42056f11eda1610242ac110002",
            "clientToken": "79fa97e3-c48b-xxxx-9f46-6a13d8163678",
            "name": "vpc-for-test-wowop",
            "CIDR": "192.168.0.0/16",
            "enableIpv6": False
        }))
        assert resp.status_code == 800
        cls.vpc_id = resp.return_obj.vpc_id
    
    def test_list_vpc(self):
        resp = self.client.describe_vpcs(ListVPCParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002'
        }))
        self.assertEqual(800, resp.status_code)
        data = resp.return_obj.model_dump(by_alias=True)
        self.assertIn('totalCount', data)
        self.assertIn('vpcs', data)
        self.assertIn('currentCount', data)
        self.assertIn('totalPage', data)
        
        for vpc in data['vpcs']:
            self.assertIn('vpcID', vpc)
            self.assertIn('name', vpc)
            self.assertIn('description', vpc)
            self.assertIn('CIDR', vpc)
            self.assertIn('ipv6Enabled', vpc)
            self.assertIn('enableIpv6', vpc)
            self.assertIn('ipv6CIDRS', vpc)
            self.assertIn('subnetIDs', vpc)
            self.assertIn('natGatewayIDs', vpc)
            self.assertIn('secondaryCIDRS', vpc)
            self.assertIn('projectID', vpc)
    
    def test_show_vpc(self):
        resp = self.client.show_vpc(ShowVPCParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'vpcID': self.vpc_id
        }))
        self.assertEqual(800, resp.status_code)
        vpc = resp.return_obj.model_dump(by_alias=True)
        self.assertIn('vpcID', vpc)
        self.assertIn('name', vpc)
        self.assertIn('description', vpc)
        self.assertIn('CIDR', vpc)
        self.assertIn('ipv6Enabled', vpc)
        self.assertIn('enableIpv6', vpc)
        self.assertIn('ipv6CIDRS', vpc)
        self.assertIn('subnetIDs', vpc)
        self.assertIn('natGatewayIDs', vpc)
        self.assertIn('secondaryCIDRS', vpc)
        self.assertIn('projectID', vpc)
        
    def test_update_vpc(self):
        resp = self.client.update_vpc(UpdateVPCParam(**{
            'clientToken': 'sssss',
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'vpcID': self.vpc_id,
            'name': 'test-test'
        }))
        self.assertEqual(800, resp.status_code)
        resp = self.client.show_vpc(ShowVPCParam(**{
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'vpcID': self.vpc_id
        }))
        self.assertEqual(800, resp.status_code)
        self.assertEqual('test-test', resp.return_obj.name)
        
    def test_update_ipv6_status(self):
        resp = self.client.update_vpc_ipv6(UpdateVPCIPv6StatusParam(**{
            'clientToken': 'sssss',
            'regionID': 'bb9fdb42056f11eda1610242ac110002',
            'vpcID': self.vpc_id,
            'enableIpv6': True
        }))
        self.assertEqual(800, resp.status_code)
    
    @classmethod
    def tearDownClass(cls) -> None:
        if cls.client:
            resp = cls.client.delete_vpc(DeleteVPCParam(**{'vpcID': cls.vpc_id, 'regionID': 'bb9fdb42056f11eda1610242ac110002'}))
            assert resp.status_code == 800
