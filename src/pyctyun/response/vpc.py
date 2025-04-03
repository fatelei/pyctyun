from typing import List, Optional

from pydantic import BaseModel, Field

from .base import BaseResponse

__all__ = [
    'CreateVpcResponse',
    'ListVpcResponse',
    'ShowVpcResponse'
]


class CreateVpc(BaseModel):
    vpc_id: str = Field(alias='vpcID')


class Vpc(BaseModel):
    vpc_id: str = Field(alias='vpcID')
    name: str
    description: str
    cidr: str = Field(alias='CIDR')
    ipv6_enabled: bool = Field(alias='ipv6Enabled')
    enable_ipv6: bool = Field(alias='enableIpv6')
    ipv6_cidrs: List[str] = Field(alias='ipv6CIDRS')
    subnet_ids: List[str] = Field(alias='subnetIDs')
    nat_gateway_ids: List[str] = Field(alias='natGatewayIDs')
    secondary_cidrs: List[str] = Field(alias='secondaryCIDRS')
    project_id: str = Field(alias='projectID')


class ListVpc(BaseModel):
    vpcs: List[Vpc]
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class CreateVpcResponse(BaseResponse):
    return_obj: Optional[CreateVpc] = Field(None, alias='returnObj')


class ListVpcResponse(BaseResponse):
    return_obj: Optional[ListVpc] = Field(None, alias='returnObj')


class ShowVpcResponse(BaseResponse):
    return_obj: Optional[Vpc] = Field(None, alias='returnObj')
