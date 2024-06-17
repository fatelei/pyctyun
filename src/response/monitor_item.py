from typing import List

from pydantic import BaseModel, Field

from .base import BaseResponse


class Item(BaseModel):

    name: str
    desc: str
    unit: str



class MonitorItem(BaseModel):

    device_type: str = Field(alias="deviceType")
    items: List[Item]


class MonitorItemReturnObj(BaseModel):
    monitor_items: List[MonitorItem] = Field(alias='monitorItems')


class MonitorItemResponse(BaseResponse):

    return_obj: MonitorItemReturnObj = Field(alias='returnObj')
