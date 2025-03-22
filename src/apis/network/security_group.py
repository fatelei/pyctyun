from src.apis.base import CtapiBaseClient

from src.param import security_group
from src.response.base import BaseResponse
from src.response.security_group import CreateSecurityGroupResponse, ListSgResponse, NewListSgResponse, \
    ShowSgResponse


class SecurityGroupApi(CtapiBaseClient):
    
    def create_security_group(self, param: security_group.CreateSecurityGroupParam) -> CreateSecurityGroupResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create-security-group', params=params, method='POST')
        return CreateSecurityGroupResponse(**data)
    
    def delete_security_group(self, param: security_group.RemoveSecurityGroupParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/delete-security-group', params=params, method='POST')
        return BaseResponse(**data)
    
    def list_security_group(self, param: security_group.ListSecurityGroupsParam) -> ListSgResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/query-security-groups', params=params, method='GET')
        return ListSgResponse(**data)
    
    def new_list_security_group(self, param: security_group.ListSecurityGroupsParam) -> NewListSgResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/new-query-security-groups', params=params, method='GET')
        return NewListSgResponse(**data)
    
    def update_security_group(self, param: security_group.UpdateSecurityGroupParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/modify-security-group-attribute', params=params, method='POST')
        return BaseResponse(**data)
    
    def show_security_group(self, param: security_group.GetSecurityGroupParam) -> ShowSgResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/describe-security-group-attribute', params=params, method='GET')
        return ShowSgResponse(**data)
    
    def bind_security_group(self, param: security_group.BindSecurityGroupParam) -> BaseResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/vpc/join-security-group', params=params, method='POST')
        return BaseResponse(**data)
    
    def unbind_security_group(self, param: security_group.UnbindSecurityGroupParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/leave-security-group', params=params, method='POST')
        return BaseResponse(**data)
    
    def batch_bind_security_group(self, param: security_group.BatchAttachSecurityGroupPortsParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/batch-attach-security-group-ports', params=params, method='POST')
        return BaseResponse(**data)
    
    def batch_unbind_security_group(self, param: security_group.BatchDetachSecurityGroupPortsParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/batch-detach-security-group-ports', params=params, method='POST')
        return BaseResponse(**data)
    
    def port_batch_unbind_sgs(self, param: security_group.BatchUnBindSecurityGroupParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/port-batch-unbind-sgs', params=params, method='POST')
        return BaseResponse(**data)
    
    def create_ingress_rule(self, param: security_group.CreateSecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create-security-group-ingress', params=params, method='POST')
        return BaseResponse(**data)
    
    def create_egress_rule(self, param: security_group.CreateSecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/create-security-group-egress', params=params, method='POST')
        return BaseResponse(**data)

    def delete_ingress_rule(self, param: security_group.RemoveSecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/revoke-security-group-ingress', params=params, method='POST')
        return BaseResponse(**data)
    
    def delete_egress_rule(self, param: security_group.RemoveSecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/revoke-security-group-egress', params=params, method='POST')
        return BaseResponse(**data)
    
    def update_ingress_rule(self, param: security_group.ModifySecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/modify-security-group-ingress', params=params, method='POST')
        return BaseResponse(**data)

    def update_egress_rule(self, param: security_group.ModifySecurityGroupRuleParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/modify-security-group-egress', params=params, method='POST')
        return BaseResponse(**data)
