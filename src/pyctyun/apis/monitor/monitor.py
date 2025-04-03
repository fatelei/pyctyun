from pyctyun.apis.base import CtapiBaseClient

from pyctyun.param.monitor import RealtimeMonitorParam
from pyctyun.response.monitor import RealtimeMetricResponse


class MonitorApi(CtapiBaseClient):
    
    def get_realtime_metric(self, param: RealtimeMonitorParam):
        params = param.model_dump(by_alias=True)
        data = self.perform_request("/v4.1/monitor/query-eip-latestmetricdata",
                                    params,
                                    method='POST')
        return RealtimeMetricResponse(**data)
