from typing import List

from pydantic import BaseModel, Field

from .base import BaseResponse


class Item(BaseModel):
    item_name: str = Field(alias='itemName')
    value: str
    sampling_time: str = Field(alias='samplingTime')


class MonitorItem(BaseModel):
    region_id: str = Field(alias="regionID")
    device_uuid: str = Field(alias='deviceUUID')
    item_list: List[Item] = Field(alias='itemList')


class RealtimeMetricItem(BaseModel):
    result: List[MonitorItem]


class RealtimeMetricResponse(BaseResponse):
    return_obj: RealtimeMetricItem = Field(alias='returnObj')
