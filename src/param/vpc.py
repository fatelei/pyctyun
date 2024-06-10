from typing import Optional

from pydantic import Field, field_validator, StrictBool, StrictStr

from src.rules.rule import BaseParamModel, PaginationGetParamModel, check_name, check_description, \
    check_vpc_cidr


class CreateVPCParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    name: StrictStr
    description: Optional[StrictStr] = None
    cidr: StrictStr = Field(alias='CIDR', min_length=1)
    enable_ipv6: Optional[StrictBool] = Field(False, alias='enableIpv6')
    ipv6_segment_pool_id: Optional[StrictStr] = Field(None, alias='ipv6SegmentPoolID')
    
    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)
    _check_cidr = field_validator('cidr')(check_vpc_cidr)


class DeleteVPCParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)


class ShowVPCParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)
    project_id: StrictStr = Field('0', alias='projectID')


class ListVPCParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: Optional[StrictStr] = Field(None, alias='vpcID')
    vpc_name: Optional[StrictStr] = Field(None, alias='vpcName')
    project_id: StrictStr = Field('0', alias='projectID')


class UpdateVPCIPv6StatusParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)
    enable_ipv6: StrictBool = Field(alias='enableIpv6')


class UpdateVPCParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)
    name: Optional[StrictStr] = Field(max_length=31, min_length=2)
    description: Optional[StrictStr] = None
    
    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)
