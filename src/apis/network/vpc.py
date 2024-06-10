from src.apis.base import CtapiBaseClient

from src.param import vpc
from src.response.base import BaseResponse
from src.response.vpc import CreateVpcResponse, ListVpcResponse, ShowVpcResponse


class VpcApi(CtapiBaseClient):
    
    def create_vpc(self, param: vpc.CreateVPCParam) -> CreateVpcResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create', params=params, method='POST')
        return CreateVpcResponse(**data)
    
    def delete_vpc(self, param: vpc.DeleteVPCParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/delete', params=params, method='POST')
        return BaseResponse(**data)
    
    def describe_vpcs(self, param: vpc.ListVPCParam) -> ListVpcResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/new-list', params=params, method='GET')
        return ListVpcResponse(**data)
    
    def show_vpc(self, param: vpc.ShowVPCParam) -> ShowVpcResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/query', params=params, method='GET')
        return ShowVpcResponse(**data)
    
    def update_vpc(self, param: vpc.UpdateVPCParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/update', params=params, method='POST')
        return BaseResponse(**data)
    
    def update_vpc_ipv6(self, param: vpc.UpdateVPCIPv6StatusParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/update-ipv6-status', params=params, method='POST')
        return BaseResponse(**data)
