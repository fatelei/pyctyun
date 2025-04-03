from typing import List, Optional

from pydantic import conint, Field, StrictStr, field_validator

from pyctyun.rules.rule import BaseParamModel, check_description, check_dns_name, check_proxy_pattern, \
    check_uuid, PaginationGetParamModel


class CreateZoneParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_ids: StrictStr = Field(alias='vpcIDList', min_length=1)
    name: StrictStr = Field(min_length=1)
    description: Optional[StrictStr]
    proxy_pattern: Optional[StrictStr] = Field('zone', alias='proxyPattern')
    ttl: Optional[conint(strict=True, ge=300, le=2147483647)] = Field(300, alias='TTL')
    
    _check_name = field_validator('name')(check_dns_name)
    _check_description = field_validator('description')(check_description)
    _check_proxy_pattern = field_validator('proxy_pattern')(check_proxy_pattern)
    
    @field_validator('vpc_ids')
    def check_vpc_ids(cls, v):
        ary = v.split(',')
        if len(ary) > 5:
            raise ValueError("only support 5 vpcs")
        
        for i in ary:
            check_uuid(i)
        return v


class DeleteZoneParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)


class ShowZoneParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)


class ListZoneParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: Optional[StrictStr] = Field(alias='zoneID')
    zone_name: Optional[StrictStr] = Field(alias='zoneName')


class ModifyZoneParam(BaseParamModel):
    client_token: Optional[StrictStr] = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    vpc_ids: Optional[StrictStr] = Field(alias='vpcIDList')
    description: Optional[StrictStr]
    proxy_pattern: Optional[StrictStr] = Field(alias='proxyPattern')
    ttl: Optional[conint(strict=True, ge=300, le=2147483647)] = Field(alias='TTL')
    
    _check_description = field_validator('description')(check_description)
    _check_proxy_pattern = field_validator('proxy_pattern')(check_proxy_pattern)
    
    @field_validator('vpc_ids')
    def check_vpc_ids(cls, v):
        if not v:
            return v
        ary = v.split(',')
        if len(ary) > 5:
            raise ValueError("only support 5 vpcs")
        
        for i in ary:
            check_uuid(i)
        return v


class BindOrUnBindZoneParam(BaseParamModel):
    client_token: Optional[StrictStr] = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    vpc_ids: StrictStr = Field(alias='vpcIDList', min_length=1)
    
    @field_validator('vpc_ids')
    def check_vpc_ids(cls, v):
        ary = v.split(',')
        if len(ary) > 5:
            raise ValueError("only support 5 vpcs")
        
        for i in ary:
            check_uuid(i)
        return v


class CheckZoneNameParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_name: StrictStr = Field(alias='zoneName', min_length=1)


class CheckTxtParam(BaseParamModel):
    txt_records: List[StrictStr] = Field(alias='txtRecords', min_items=1, max_items=10, min_length=1)


class CheckMxParam(BaseParamModel):
    mx_records: List[StrictStr] = Field(alias='mxRecords', min_items=1, max_items=10, min_length=1)


class CheckCnameParam(BaseParamModel):
    cname_records: List[StrictStr] = Field(alias='cnameRecords', min_items=1, max_items=10, min_length=1)


class CheckPtrParam(BaseParamModel):
    ptr_records: List[StrictStr] = Field(alias='ptrRecords', min_items=1, max_items=10, min_length=1)


class CheckSrvParam(BaseParamModel):
    srv_records: List[StrictStr] = Field(alias='srvRecords', min_items=1, max_items=10, min_length=1)


class Check4AParam(BaseParamModel):
    aaaa_records: List[StrictStr] = Field(alias='aaaaRecords', min_items=1, max_items=10, min_length=1)


class ListZoneRecordParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: Optional[StrictStr] = Field(alias='zoneID')
    zone_record_id: Optional[StrictStr] = Field(alias='zoneRecordID')


class SetZonePatternParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    proxy_pattern: StrictStr = Field(alias='proxyPattern', min_length=1)
    
    _check_proxy_pattern = field_validator('proxy_pattern')(check_proxy_pattern)


class GetZoneLabelsParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)


class ZoneBindLabelParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    label_key: StrictStr = Field(alias='labelKey', min_length=1)
    label_value: StrictStr = Field(alias='labelValue', min_length=1)


class ZoneUnBindLabelParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    zone_id: StrictStr = Field(alias='zoneID', min_length=1)
    label_id: StrictStr = Field(alias='labelID', min_length=1)


class GetVpcBindedZonesParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)


class GetAllZonesAndVpcsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
