from pydantic import BaseModel, Field, StrictStr


class DeleteRouteRuleParam(BaseModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    route_rule_id: StrictStr = Field(min_length=1, alias="routeRuleID")
