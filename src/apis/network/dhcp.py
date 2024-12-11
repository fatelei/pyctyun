from src.apis.base import CtapiBaseClient

from src.param import dhcp
from src.response import dhcp as dhcp_response


class DhcpApi(CtapiBaseClient):
    
    def create_dhcp(self, param: dhcp.CreateDhcpoptionSetsParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/create', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def delete_dhcp(self, param: dhcp.DeleteDhcpoptionSetsParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/delete', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def update_dhcp(self, param: dhcp.UpdateDhcpoptionSetsParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/dhcpoptionsets/update', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def show_dhcp(self, param: dhcp.ShowDhcpoptionSetsParam) -> dhcp_response.ShowDhcpResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/show', params=params, method='GET')
        return dhcp_response.ShowDhcpResponse(**data)
    
    def list_dhcp(self, param: dhcp.DhcpoptionListVpcParam) -> dhcp_response.ListDhcpResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/dhcpoptionsets/query', params=params, method='GET')
        return dhcp_response.ListDhcpResponse(**data)
    
    def dhcp_associate_vpc(self, param: dhcp.DhcpoptionWithVpcParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/dhcp_associate_vpc', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def dhcp_disassociate_vpc(self, param: dhcp.DhcpoptionWithVpcParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/dhcp_disassociate_vpc', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def dhcp_replace_vpc(self, param: dhcp.DhcpoptionWithVpcParam) -> dhcp_response.DhcpOptionSetIDResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/dhcpoptionsets/dhcp_replace_vpc', params=params, method='POST')
        return dhcp_response.DhcpOptionSetIDResponse(**data)
    
    def dhcp_list_unbind_vpc(self, param: dhcp.DhcpoptionListUnbindVpcParam) -> dhcp_response.UnbindVpcResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/dhcpoptionsets/dhcp_list_unbind_vpc', params=params, method='GET')
        return dhcp_response.ListDhcpResponse(**data)
    
    def dhcp_list_vpc(self, param: dhcp.DhcpoptionListVpcParam) -> dhcp_response.BindVpcResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/dhcpoptionsets/dhcp_list_vpc', params=params, method='GET')
        return dhcp_response.BindVpcResponse(**data)
