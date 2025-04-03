from pyctyun.apis.base import CtapiBaseClient

from pyctyun.param import subnet
from pyctyun.response.base import BaseResponse
from pyctyun.response.subnet import CreateSubnetResponse, NewListSubnetResponse, ListSubnetResponse, ShowSubnetResponse, \
    CheckIpAvailableResponse


class SubnetApi(CtapiBaseClient):
    
    def create_subnet(self, param: subnet.CreateSubnetParam) -> CreateSubnetResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create-subnet', params=params, method='POST')
        return CreateSubnetResponse(**data)
    
    def delete_subnet(self, param: subnet.DeleteSubnetParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/delete-subnet', params=params, method='POST')
        return BaseResponse(**data)
    
    def enable_ipv6(self, param: subnet.SubnetEnableIPv6Param) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/subnet-enable-ipv6', params=params, method='POST')
        return BaseResponse(**data)
    
    def replace_acl(self, param: subnet.SubnetReplaceACLParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/replace-subnet-acl', params=params, method='POST')
        return BaseResponse(**data)
    
    def replace_route_table(self, param: subnet.SubnetReplaceRouteTableParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/replace-subnet-route-table', params=params, method='POST')
        return BaseResponse(**data)
    
    def disassociate_acl(self, param: subnet.SubnetDisassociateACLParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/disassociate-subnet-acl', params=params, method='POST')
        return BaseResponse(**data)
    
    def disassociate_route_table(self, param: subnet.SubnetDisassociateRouteTableParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/subnet-disassociate-route-table', params=params, method='POST')
        return BaseResponse(**data)
    
    def show_subnet(self, param: subnet.ShowSubnetParam) -> ShowSubnetResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/query', params=params, method='GET')
        return ShowSubnetResponse(**data)
    
    def new_list_subnets(self, param: subnet.ListSubnetsParam) -> NewListSubnetResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/new-list-subnet', params=params, method='GET')
        return NewListSubnetResponse(**data)
    
    def list_subnets(self, param: subnet.ListSubnetsParam) -> ListSubnetResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/list-subnet', params=params, method='GET')
        return ListSubnetResponse(**data)
    
    def check_ip_avaliable(self, param: subnet.CheckIpAvaliableParam) -> CheckIpAvailableResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/check-ip-avaliable', params=params, method='GET')
        return CheckIpAvailableResponse(**data)
