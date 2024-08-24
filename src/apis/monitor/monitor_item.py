from src.apis.base import CtapiBaseClient

from src.param.montior_item import MonitorItemParam
from src.response.monitor_item import MonitorItemResponse


class MonitorItemApi(CtapiBaseClient):
    
    def get_monitor_items(self, param: MonitorItemParam):
        params = param.model_dump(by_alias=True, exclude_none=True)
        data = self.perform_request("/v4/monitor/query-monitor-items",
                                    params,
                                    method='GET')
        return MonitorItemResponse(**data)
