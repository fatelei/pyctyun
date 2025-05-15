from pyctyun.apis.base import CtapiBaseClient

from pyctyun.param import vpc_peer
from pyctyun.response.base import BaseResponse
from pyctyun.response.vpc_peer import ListVpcPeerRequestResponse, CreateVpcPeerResponse, ListVpcPeerResponse, NewListVpcPeerResponse, \
    ShowVpcPeerResponse


class VpcPeerApi(CtapiBaseClient):
    
    def create_vpc_peer(self, param: vpc_peer.CreateVPCPeerParam) -> CreateVpcPeerResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create-vpc-peer-connection', params=params, method='POST')
        return CreateVpcPeerResponse(**data)
    
    def update_vpc_peer(self, param: vpc_peer.ModifyVpcPeeringParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/modify-vpc-peer-connection', params=params, method='POST')
        return BaseResponse(**data)
    
    def delete_vpc_peer(self, param: vpc_peer.DeleteVpcPeeringParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/delete-vpc-peer-connection', params=params, method='POST')
        return BaseResponse(**data)
    
    def agree_create_vpc_peer(self, param: vpc_peer.AcceptOrRejectVpcPeerRequestParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/vpcpeer/agree-request', params=params, method='POST')
        return BaseResponse(**data)
    
    def refuse_create_vpc_peer(self, param: vpc_peer.AcceptOrRejectVpcPeerRequestParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/vpcpeer/reject-request', params=params, method='POST')
        return BaseResponse(**data)
    
    def new_list_vpc_peer(self, param: vpc_peer.ListVpcPeeringParam) -> NewListVpcPeerResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/new-list-vpc-peer-connection', params=params, method='GET')
        return NewListVpcPeerResponse(**data)
    
    def list_vpc_peer(self, param: vpc_peer.ListVpcPeeringParam) -> ListVpcPeerResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/list-vpc-peer-connection', params=params, method='GET')
        return ListVpcPeerResponse(**data)
    
    def show_vpc_peer(self, param: vpc_peer.ShowVpcPeeringParam) -> ShowVpcPeerResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/get-vpc-peer-connection-attribute', params=params, method='GET')
        return ShowVpcPeerResponse(**data)
    
    def list_vpc_peer_requests(self, param: vpc_peer.ListUnHandlePeeringRequestParam) -> ListVpcPeerRequestResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/vpcpeer/requests', params=params, method='GET')
        return ListVpcPeerRequestResponse(**data)
    
    
    
    
    