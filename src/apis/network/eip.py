from src.apis.base import CtapiBaseClient

from src.param import eip
from src.response.eip import ListEipResponse, NewListEipResponse


class EipApi(CtapiBaseClient):
    
    def list_eip(self, param: eip.ListEipParam) -> ListEipResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/eip/list', params=params, method='POST')
        return ListEipResponse(**data)
    
    def new_list_eip(self, param: eip.ListEipParam) -> NewListEipResponse:
        params = param.model_dump(by_alias=True)
        data = self.perform_request('/v4/eip/new-list', params=params, method='POST')
        return NewListEipResponse(**data)
