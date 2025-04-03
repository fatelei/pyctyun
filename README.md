# pyctyun
ctyun.cn openapi implement in python

[x] support vpc api.

## example
```python
>>> from pyctyun.apis.network.eip import EipApi
>>> from pyctyun.param import eip
>>> a = EipApi(ak='input your sk', sk='input your sk', endpoint='https://ctvpc-global.ctapi.ctyun.cn')
>>> param = eip.ListEipParam(regionID='200000001781', clientToken='sss')
>>> a.list_eip(param)
ListEipResponse(status_code=800, message='success', description='成功', error_code='SUCCESS', return_obj=ListEip(eips=[Eip(id='eip-5ink7wj2ab', name='eip-da41', eip_address='203.2.67.71', association_id='', association_type=None, private_ip_address=None, bandwidth=1, bandwidth_id='', bandwidth_type='standalone', status='DOWN', tags='', created_at='2025-03-14T09:12:44Z', updated_at='2025-03-14T09:12:48Z', expired_at=None)]), total_count=1, current_count=1, total_page=1)
```