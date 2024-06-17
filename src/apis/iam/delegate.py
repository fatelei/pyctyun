from typing import List, Dict

from dataclasses import dataclass

from src.apis.base import CtapiBaseClient


@dataclass
class QueryDelegateRoleParam:
    user_id: str
    
    
@dataclass
class DelegateRoleResponse:
    
    account_id: str
    role_list: List[str]
    role_info: Dict


class DelegateApi(CtapiBaseClient):
    
    def query_delegate_role(self, param: QueryDelegateRoleParam, headers=None, timeout=1):
        params = {
            "assumeUserId": param.user_id,
        }
        data = self.perform_request('/v1/delegate/queryDelegateRoleValue', params, 'POST', headers=headers, timeout=timeout)
        if data['statusCode'] == '800':
            return_obj = data.get("returnObj") or {}
            account_id = return_obj.get("assumeAccountId")
            role_list = return_obj.get("roleList", [])
            role_code_list = []
            role_info = {}
            for role in role_list:
                role_code = role.get("roleCode")
                role_code_list.append(role_code)
                role_info[role_code] = [item["value"] for item in role.get("valueList", []) if 'value' in item]
    
            return DelegateRoleResponse(
                account_id=account_id,
                role_list=role_code_list,
                role_info=role_info
            )
        return DelegateRoleResponse(
            account_id='',
            role_list=[],
            role_info={}
        )
