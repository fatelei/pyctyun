import unittest

from src.rules import rule


class TestRules(unittest.TestCase):
    
    def test_check_cycle_count(self):
        rule.check_cycle_count(1, {"cycle_type": 'year'})
        rule.check_cycle_count(1, {"cycle_type": 'month'})
        rule.check_cycle_count(1, {'cycle_type': 'on_demand'})
        
        with self.assertRaises(ValueError):
            rule.check_cycle_count(4, {"cycle_type": 'year'})
            
        with self.assertRaises(ValueError):
            rule.check_cycle_count(12, {"cycle_type": 'month'})
            
    def test_check_dns_name(self):
        rule.check_dns_name("a.b.c")
        with self.assertRaises(ValueError):
            rule.check_dns_name("a" * 255)
            
        with self.assertRaises(ValueError):
            a = 'a' * 64
            rule.check_dns_name(f'{a}.c')
            
    def test_check_aaaa(self):
        rule.check_aaaa("E24D:0D46:B5D1:FEBE:1CD8:0BD6:D8A3:6C27")
        with self.assertRaises(ValueError):
            rule.check_aaaa("192.168.1.1")
        
    def test_check_uuid(self):
        rule.check_uuid("a-b-c-d")
        
        with self.assertRaises(ValueError):
            rule.check_uuid("AAAAA")
            
    def test_check_uuids(self):
        rule.check_uuids(["a-b-c-d"])
        with self.assertRaises(ValueError):
            rule.check_uuids(["AAAAA"])
            
    def test_check_email(self):
        rule.check_email("foo@bar.com")
        with self.assertRaises(ValueError):
            rule.check_email("sdsdsds")
