from typing import Optional, List

from pydantic import BaseModel, Field

from .base import BaseResponse

__all__ = [
    'CreateSubnetResponse',
    "ListSubnetResponse",
    "NewListSubnetResponse",
    "ShowSubnetResponse",
    "CheckIpAvailableResponse"
]


class CreateSubnet(BaseModel):
    vpc_id: str = Field(alias='vpcID')


class CreateSubnetResponse(BaseResponse):
    return_obj: Optional[CreateSubnet] = Field(None, alias='returnObj')


class Subnet(BaseModel):
    subnet_id: str = Field(alias="subnetID")
    name: str
    description: str
    vpc_id: str = Field(alias="vpcID")
    availability_zones: List[str] = Field(alias="availabilityZones")
    route_table_id: str = Field(alias="routeTableID")
    acl_id: str = Field(alias="networkAclID")
    cidr: str = Field(alias="CIDR")
    gateway_ip: str = Field(alias="gatewayIP")
    start: str
    end: str
    available_ip_count: int = Field(alias="availableIPCount")
    ipv6_enabled: int = Field(alias="ipv6Enabled")
    enable_ipv6: bool = Field(alias="enableIpv6")
    ipv6_cidr: str = Field(alias="ipv6CIDR")
    ipv6_start: str = Field(alias="ipv6Start")
    ipv6_end: str = Field(alias="ipv6End")
    ipv6_gateway_ip: str = Field(alias="ipv6GatewayIP")
    dns_list: List[str] = Field(alias="dnsList")
    ntp_list: List[str] = Field(alias="ntpList")
    type: int
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")


class ListSubnetResponse(BaseResponse):
    return_obj: Optional[List[Subnet]] = Field(None, alias='returnObj')
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class ListSubnets(BaseModel):
    subnets: List[Subnet]
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class NewListSubnetResponse(BaseResponse):
    return_obj: ListSubnets = Field(alias='returnObj')


class ShowSubnetResponse(BaseResponse):
    return_obj: Subnet = Field(None, alias='returnObj')


class IpAvailable(BaseModel):
    is_available: bool = Field(alias="isAvailable")


class CheckIpAvailableResponse(BaseResponse):
    return_obj: IpAvailable = Field(None, alias='returnObj')
