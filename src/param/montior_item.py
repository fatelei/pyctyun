from pydantic import Field

from src.rules.rule import BaseParamModel


class MonitorItemParam(BaseParamModel):

    device_type: str = Field(alias="deviceType", min_length=1)
