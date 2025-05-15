from typing import Optional
from pydantic import BaseModel, Field

from .base import BaseResponse


class CreateVpcPeerReturnObj(BaseModel):
    status: str
    message: str
    instance_id: str = Field(alias="instanceID")


class CreateVpcPeerResponse(BaseResponse):
    return_obj: Optional[CreateVpcPeerReturnObj] = Field(None, alias="returnObj")


class DeleteVpcPeerReturnObj(BaseModel):
    status: str
    message: str

    
class DeleteVpcPeerResponse(BaseResponse):
    return_obj: Optional[DeleteVpcPeerReturnObj] = Field(None, alias="returnObj")
    

class VpcPeer(BaseModel):

    name: str
    instance_id: str = Field(alias="instanceID")
    status: str
    request_vpc_id: str = Field(alias="requestVpcID")
    request_vpc_cidr: str = Field(alias="requestVpcCidr")
    request_vpc_name: str = Field(alias="requestVpcName")
    accept_vpc_id: str = Field(alias="acceptVpcID")
    accept_vpc_cidr: str = Field(alias="acceptVpcCidr")
    accept_vpc_name: str = Field(alias="acceptVpcName")
    user_type: str = Field(alias="userType")
    accept_email: str = Field(alias="acceptEmail")
    creation_time: str = Field(alias="creationTime")
    status: Optional[str]
    
    
class ListVpcPeerResponse(BaseResponse):
    return_obj: list[VpcPeer] = Field(alias="returnObj")
    current_count: int = Field(alias="currentCount")
    total_count: int = Field(alias="totalCount")
    total_page: int = Field(alias="totalPage")


class NewListVpcPeerReturnObj(BaseModel):
    results: list[VpcPeer]
    current_count: int = Field(alias="currentCount")
    total_count: int = Field(alias="totalCount")
    total_page: int = Field(alias="totalPage")


class NewListVpcPeerResponse(BaseResponse):
    return_obj: NewListVpcPeerReturnObj = Field(alias="returnObj")
    

class ShowVpcPeerResponse(BaseResponse):
    return_obj: VpcPeer
    
    
class VpcPeerRequest(BaseModel):
    instance_id: str = Field(alias="instanceID")
    equest_vpc_id: str = Field(alias="requestVpcID")
    request_vpc_cidr: str = Field(alias="requestVpcCidr")
    request_vpc_name: str = Field(alias="requestVpcName")
    accept_vpc_id: str = Field(alias="acceptVpcID")
    accept_vpc_cidr: str = Field(alias="acceptVpcCidr")
    accept_vpc_name: str = Field(alias="acceptVpcName")
    status: str
    
    
class ListVpcPeerRequestReturnObj(BaseModel):
    vpc_peer_requests: list[VpcPeerRequest] = Field(alias="vpcPeerRequests")
    current_count: int = Field(alias="currentCount")
    total_count: int = Field(alias="totalCount")
    total_page: int = Field(alias="totalPage")
    
    
class ListVpcPeerRequestResponse(BaseResponse):
    return_obj: ListVpcPeerRequestReturnObj = Field(alias="returnObj")
