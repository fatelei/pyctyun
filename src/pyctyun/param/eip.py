from typing import Optional

from pydantic import Field, field_validator, StrictStr

from pyctyun.rules.rule import PaginationGetParamModel, check_ip


class ListEipParam(PaginationGetParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    ids: Optional[list[StrictStr]] = None
    status: Optional[StrictStr] = None
    ip_type: Optional[StrictStr] = Field('ipv4', alias='ipType')
    eip_type: Optional[StrictStr] = Field('normal', alias='eipType')
    ip: Optional[StrictStr] = None
    include_device: bool = Field(False, alias='includeDevice')
    
    _check_address = field_validator('ip')(check_ip)
    
    @field_validator('status')
    def check_status(cls, value):
        status = ['ACTIVE', 'DOWN', 'FREEZING', 'EXPIRED']
        if value and value not in status:
            raise ValueError("only support ACTIVE / DOWN / EXPIRED / FREEZING")
        return value
    
    @field_validator('ip_type')
    def check_ip_type(cls, value):
        if value and value not in ['ipv4', 'ipv6']:
            raise ValueError('should be ipv4 or ipv6')
        return value
    
    @field_validator('eip_type')
    def check_eip_type(cls, value):
        if value and value not in ['normal', 'cn2']:
            raise ValueError('should be normal or cn2')
        return value