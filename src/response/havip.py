from typing import Optional, List

from pydantic import BaseModel, Field

from .base import BaseResponse

__all__ = [
    'CreateHavipResponse',
    "ListHavipResponse",
    "ShowHavipResponse"
]


class CreateHavip(BaseModel):
    havip_id: str = Field(alias='uuid')
    ipv4: str
    ipv6: str


class NetworkInfo(BaseModel):
    
    eip_id: str = Field(alias="eipID")


class BindPorts(BaseModel):
    port_id: str = Field(alias="portID")
    role: str
    created_at: str = Field(alias="createdAt")


class InstanceInfo(BaseModel):
    
    instance_name: str = Field(alias="instanceName")
    id: str
    private_ip: str = Field(alias="privateIp")
    private_ipv6: str = Field(alias="privateIpv6")
    public_ip: str = Field(alias="publicIp")


class Havip(BaseModel):

    id: str
    ipv4: str
    vpc_id: str = Field(alias="vpcID")
    subnet_id: str = Field(alias="subnetID")
    instance_info: List[InstanceInfo] = Field(alias="instanceInfo")
    bind_ports: List[BindPorts] = Field([], alias="bindPorts")
    network_info: List[NetworkInfo] = Field([], alias="networkInfo")


class CreateHavipResponse(BaseResponse):
    return_obj: Optional[CreateHavip] = Field(None, alias='returnObj')
    
    
class ListHavipResponse(BaseResponse):
    return_obj: List[Havip] = Field(None, alias='returnObj')
    
    
class ShowHavipResponse(BaseResponse):
    return_obj: Havip = Field(None, alias='returnObj')