import logging

from dataclasses import dataclass
from typing import Optional

from src import exceptions
from src.apis.base import CtapiBaseClient

logger = logging.getLogger('')

@dataclass
class CheckUserPermissionParam:
    
    action: str
    user_id: str
    account_id: str
    region_id: Optional[str] = None
    project_id: Optional[str] = None


class IamApi(CtapiBaseClient):

    def check_user_permission(self, param: CheckUserPermissionParam, headers=None, timeout=1):
        params = {
            "action": param.action,
            "assumeUserId": param.user_id,
            "accountId": param.account_id,
            "regionCode": param.region_id,
            "epId": param.project_id,
        }
        try:
            data = self.perform_request('/v1/perm/validate', params, 'POST', headers=headers, timeout=timeout)
            if data['statusCode'] == 'CTIAM_0005':
                return False
            return True
        except exceptions.CtapiException as e:
            logger.warning(f'ctapi error {str(e)}', exc_info=True)
            return False
