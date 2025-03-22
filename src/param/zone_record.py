from typing import List, Optional

from pydantic import conint, Field, StrictStr, field_validator

from src.rules.rule import BaseParamModel, check_description, \
    check_record_type, check_record_type_and_value, PaginationGetParamModel


class CreateZoneRecordParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    name: Optional[StrictStr]
    description: Optional[StrictStr]
    record_type: StrictStr = Field(alias="type", min_length=1)
    ttl: Optional[conint(strict=True, ge=300, le=2147483647)] = Field(default=300, alias='TTL')
    value_list: List[StrictStr] = Field(alias="valueList", min_items=1, max_items=8, min_length=1)
    
    _check_record_type = field_validator('record_type')(check_record_type)
    _check_description = field_validator('description')(check_description)
    
    @field_validator('value_list')
    def check_value_list(cls, v, values):
        if 'record_type' not in values:
            return v
        record_type = values['record_type']
        return check_record_type_and_value(record_type, v)


class DeleteZoneRecordParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    zone_record_id: StrictStr = Field(alias='zoneRecordID', min_length=1)


class ShowZoneRecordParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_record_id: StrictStr = Field(alias='zoneRecordID', min_length=1)


class ModifyZoneRecordParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: Optional[StrictStr] = Field(alias='clientToken', min_length=1, max_length=64)
    zone_record_id: StrictStr = Field(alias='zoneRecordID', min_length=1)
    description: Optional[StrictStr]
    ttl: Optional[conint(strict=True, ge=300, le=2147483647)] = Field(alias='TTL')
    value_list: List[StrictStr] = Field(alias="valueList", min_items=1, min_length=1)
    
    _check_description = field_validator('description')(check_description)


class ModifyZoneRecordDescParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: Optional[StrictStr] = Field(alias='clientToken', min_length=1, max_length=64)
    zone_record_id: StrictStr = Field(alias='zoneRecordID', min_length=1)
    description: Optional[StrictStr]
    
    _check_description = field_validator('description')(check_description)


class BatchDeleteZoneRecordParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    zone_record_ids: list[StrictStr] = Field(alias='zoneRecordIDs', min_items=1, max_items=10, min_length=1)


class ListSharedZoneRecordParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
