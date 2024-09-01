from src.apis.base import CtapiBaseClient

from src.param import havip
from src.response.base import BaseResponse
from src.response.havip import CreateHavipResponse, ListHavipResponse, ShowHavipResponse


class HavipApi(CtapiBaseClient):
    
    def create_havip(self, param: havip.CreateVipParam) -> CreateHavipResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/create', params=params, method='POST')
        return CreateHavipResponse(**data)
    
    def delete_havip(self, param: havip.DeleteVipParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/delete', params=params, method='POST')
        return BaseResponse(**data)
    
    def show_havip(self, param: havip.ShowVipParam) -> ShowHavipResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/show', params=params, method='GET')
        return ShowHavipResponse(**data)
    
    def list_havip(self, param: havip.ListVipParam) -> ListHavipResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/list', params=params, method='POST')
        return ListHavipResponse(**data)
    
    def bind_havip(self, param: havip.BindOrUnbindVipParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/bind', params=params, method='POST')
        return BaseResponse(**data)
    
    def unbindd_havip(self, param: havip.BindOrUnbindVipParam) -> BaseResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/vpc/havip/unbind', params=params, method='POST')
        return BaseResponse(**data)