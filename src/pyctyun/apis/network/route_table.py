from pyctyun.apis.base import CtapiBaseClient

from pyctyun.param import route_table


class RouteTableApi(CtapiBaseClient):
    
    def delete_route_rule(self, param: route_table.DeleteRouteRuleParam):
        params = param.model_dump(by_alias=True)
        data = self.perform_request("/v4/vpc/route-table/delete-rule", params=params, method="POST")
        return data
