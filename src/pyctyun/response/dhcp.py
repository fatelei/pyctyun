from typing import Optional

from pydantic import BaseModel, Field

from .base import BaseResponse


class DhcpOption(BaseModel):
    dhcp_option_sets_id: str = Field(alias='dhcpOptionSetsID')
    name: str
    description: str
    domain_name: list[str] = Field(alias="domainName")
    dns_list: list[str] = Field(alias="dnsList")
    vpc_list: list[str] = Field(alias="vpcList")
    created_at: str = Field(alias='createdAt')
    updated_at: str = Field(alias='updatedAt')


class ShowDhcpResponse(BaseResponse):
    return_obj: Optional[DhcpOption] = Field(alias='returnObj')


class ListDhcp(BaseModel):
    results: list[DhcpOption]
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class ListDhcpResponse(BaseResponse):
    return_obj: Optional[ListDhcp] = Field(alias='returnObj')


class UnbindVpc(BaseModel):
    id: str
    name: str


class UnbindVpcResponse(BaseResponse):
    return_obj: Optional[list[UnbindVpc]] = Field(alias='returnObj')


class Vpc(BaseModel):
    vpc_id: str = Field(alias='vpcID')
    name: str
    cidr: str
    status: str
    created_at: str = Field(alias='createdAt')
    secondary_cidrs: list[str] = Field(alias='secondaryCidrs')


class BindVpc(BaseModel):
    results: list[Vpc]
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class BindVpcResponse(BaseResponse):
    return_obj: Optional[BindVpc] = Field(alias='returnObj')
    
    
class DhcpOptionSetID(BaseModel):
    
    dhcp_option_sets_id: str = Field(alias='dhcpOptionSetsID')
    
    
class DhcpOptionSetIDResponse(BaseResponse):
    return_obj: Optional[DhcpOptionSetID] = Field(alias='returnObj')

