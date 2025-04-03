from pyctyun.apis.base import CtapiBaseClient

from pyctyun.param import prefix_list
from pyctyun.response import prefix_list as prefix_list_response


class PrefixListApi(CtapiBaseClient):
    
    def create_prefix_list(self, param: prefix_list.CreatePrefixListParam) -> prefix_list_response.CreatePrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/create', params=params, method='POST')
        return prefix_list_response.CreatePrefixListResponse(**data)
    
    def delete_prefix_list(self, param: prefix_list.DeletePrefixListParam) -> prefix_list_response.DeletePrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/delete', params=params, method='POST')
        return prefix_list_response.DeletePrefixListResponse(**data)
    
    def list_prefix_list(self, param: prefix_list.QueryPrefixListParam) -> prefix_list_response.ListPrefixResponse:
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request('/v4/prefixlist/query', params=params, method='GET')
        return prefix_list_response.ListPrefixResponse(**data)
    
    def show_prefix_list(self, param: prefix_list.ShowPrefixListParam) -> prefix_list_response.ShowPrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/show', params=params, method='GET')
        return prefix_list_response.ShowPrefixListResponse(**data)
    
    def clone_prefix_list(self, param: prefix_list.ClonePrefixListParam) -> prefix_list_response.ClonePrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/clone', params=params, method='POST')
        return prefix_list_response.ClonePrefixListResponse(**data)
    
    def update_prefix_list(self, param: prefix_list.UpdatePrefixListParam) -> prefix_list_response.ModifyPrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/update', params=params, method='POST')
        return prefix_list_response.ModifyPrefixListResponse(**data)
    
    def create_prefix_list_rule(self, param: prefix_list.CreatePrefixListRuleParam) -> prefix_list_response.CreatePrefixListResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist_rule/create', params=params, method='POST')
        return prefix_list_response.CreatePrefixListResponse(**data)
    
    def delete_prefix_list_rule(self, param: prefix_list.DeletePrefixListRuleParam) -> prefix_list_response.DeletePrefixListRuleResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist_rule/delete', params=params, method='POST')
        return prefix_list_response.DeletePrefixListRuleResponse(**data)
    
    def modify_prefix_list_rule(self, param: prefix_list.UpdatePrefixListRuleParam) -> prefix_list_response.UpdatePrefixListRuleResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist_rule/update', params=params, method='POST')
        return prefix_list_response.UpdatePrefixListRuleResponse(**data)
    
    def list_bind_resource(self, param: prefix_list.ListBindResourceParam) -> prefix_list_response.ListResourceResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/prefixlist/get_associations', params=params, method='GET')
        return prefix_list_response.ListResourceResponse(**data)
        