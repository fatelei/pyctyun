from typing import Optional

from pydantic import Field, field_validator, StrictStr

from src.rules.rule import check_ip, check_description, BaseParamModel


class CreateVipParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    network_id: Optional[StrictStr] = Field(alias='networkID')
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    ip_address: Optional[StrictStr] = Field(alias='ipAddress')
    vip_type: Optional[StrictStr] = Field('v4', alias='vipType')
    description: Optional[StrictStr] = Field(alias='description')
    
    _check_ip = field_validator('ip_address')(check_ip)
    _check_description = field_validator('description')(check_description)
    
    @field_validator('vip_type')
    def check_vip_type(cls, value: str):
        if value is None:
            return 'v4'
        if value is not None and value not in ('v4', 'v6'):
            raise ValueError('only support v4 / v6')
        return value


class DeleteVipParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    vip_id: StrictStr = Field(alias='haVipID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class ShowVipParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vip_id: StrictStr = Field(alias='haVipID', min_length=1)


class ListVipFilter(BaseParamModel):
    key: StrictStr
    value: StrictStr
    
    @field_validator('key', mode='after')
    def check_key(cls, v):
        if v not in ('haVipID', 'vpcID', 'subnetID'):
            raise ValueError('only support haVipID / vpcID / subnetID')
        return v


class ListVipParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    project_id: Optional[StrictStr] = Field('0', alias='projectID')
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    filters: Optional[list[ListVipFilter]] = Field(None)


class BindOrUnbindVipParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    resource_type: StrictStr = Field(alias='resourceType', min_length=1)
    ha_vip_id: StrictStr = Field(alias='haVipID', min_length=1)
    instance_id: Optional[StrictStr] = Field(None, alias='instanceID')
    network_interface_id: Optional[StrictStr] = Field(None, alias='networkInterfaceID')
    floating_id: Optional[StrictStr] = Field(None, alias='floatingID')
    project_id: StrictStr = Field('0', alias='projectID')
    
    @field_validator('resource_type', mode='after')
    def check_resource_type(cls, value: str):
        tmp = value.lower()
        if tmp not in ('vm', 'pm', 'network'):
            raise ValueError('only support VM / PM / NETWORK')
        return tmp
    
    @field_validator('network_interface_id', mode='after')
    def check_network_interface_id(cls, v, values):
        if 'resource_type' not in values.data:
            return v
        if values.data['resource_type'].lower() in ('vm', 'pm') and not v:
            raise ValueError("when resourceType is vm / pm, networkInterfaceID field required")
        return v
    
    @field_validator('instance_id', mode='after')
    def check_instance_id(cls, v, values):
        if 'resource_type' not in values.data:
            return v
        
        if values.data['resource_type'].lower() in ('vm', 'pm') and not v:
            raise ValueError("when resourceType is vm / pm, instanceID field required")
        return v
    
    @field_validator('floating_id', mode='after')
    def check_floating_id(cls, v, values):
        if 'resource_type' not in values.data:
            return v
        
        if values.data['resource_type'].lower() in ('network',) and not v:
            raise ValueError("when resourceType is NETWORK, floating_id field required")
        return v