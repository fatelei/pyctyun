from typing import Optional

from pydantic import Field

from pyctyun.rules.rule import BaseParamModel


class MonitorItemParam(BaseParamModel):

    region_id: str = Field(alias='regionID', min_length=1)
    service: Optional[str] = Field(None)
    item_type: Optional[str] = Field(None, alias='itemType')
