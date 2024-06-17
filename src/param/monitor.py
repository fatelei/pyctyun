from typing import List

from pydantic import Field

from src.rules.rule import BaseParamModel


class RealtimeMonitorParam(BaseParamModel):
    region_id: str = Field(alias='regionID', min_length=1)
    device_uud_list: List[str] = Field(alias='deviceUUIDList', min_items=1)
