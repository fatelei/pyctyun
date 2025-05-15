from typing import Optional

from pydantic import Field, field_validator, StrictStr

from pyctyun.rules.rule import BaseParamModel, PaginationGetParamModel, check_cidr, check_email, check_name, \
    check_description


class ListUnHandlePeeringRequestParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class ListVpcPeeringParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class DeleteVpcPeeringParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    vpc_peer_id: StrictStr = Field(alias='instanceID', min_length=1)


class ShowVpcPeeringParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_peer_id: StrictStr = Field(alias='instanceID', min_length=1)


class AcceptOrRejectVpcPeerRequestParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    peering_info_id: StrictStr = Field(alias='instanceID', min_length=1)


class CreateVPCPeerParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    request_vpc_id: StrictStr = Field(alias='requestVpcID', min_length=1)
    request_vpc_cidr: StrictStr = Field(alias='requestVpcCidr', min_length=1)
    request_vpc_name: StrictStr = Field(alias='requestVpcName', min_length=1)
    accept_vpc_id: StrictStr = Field(alias='acceptVpcID', min_length=1)
    accept_vpc_name: Optional[StrictStr] = Field(alias='acceptVpcName')
    accept_vpc_cidr: Optional[StrictStr] = Field(alias='acceptVpcCidr')
    accept_email: Optional[StrictStr] = Field(None, alias='acceptEmail')
    name: StrictStr = Field(min_length=1)
    
    _check_name = field_validator('name')(check_name)
    _check_email = field_validator('accept_email')(check_email)
    _check_cidr = field_validator('request_vpc_cidr')(check_cidr)


class ModifyVpcPeeringParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    vpc_peer_id: StrictStr = Field(alias='instanceID', min_length=1)
    name: Optional[StrictStr]
    description: Optional[StrictStr]
    
    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)
