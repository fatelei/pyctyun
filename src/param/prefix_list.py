from typing import Optional, List

from pydantic import Field, field_validator, StrictStr, conint, StrictInt

from src.rules.rule import check_description, BaseParamModel, check_cidr, check_name, PaginationGetParamModel


class PrefixListRule(BaseParamModel):
    cidr: StrictStr = Field(min_length=1)
    description: Optional[StrictStr]

    _check_cidr = field_validator('cidr')(check_cidr)
    _check_description = field_validator('description')(check_description)


class CreatePrefixListParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    name: StrictStr
    limit: conint(strict=True, ge=1, le=200)
    description: Optional[StrictStr]
    address_type: StrictInt = Field(alias='addressType')
    prefix_list_rules: List[PrefixListRule] = Field(alias='prefixListRules', min_items=1, max_items=200)

    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)

    @field_validator('address_type')
    def check_address_type(cls, value: int):
        if value and value not in (4, 6):
            raise ValueError('only support 4 / 6')
        return value


class QueryPrefixListParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    query_content: Optional[StrictStr] = Field(alias='queryContent', min_length=1)
    prefix_list_id: Optional[StrictStr] = Field(alias='prefixListID', min_length=1)


class ShowPrefixListParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)


class UpdatePrefixListParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
    name: Optional[StrictStr]
    description: Optional[StrictStr]

    _check_name = field_validator('name', allow_reuse=True)(check_name)
    _check_description = field_validator('description', allow_reuse=True)(check_description)


class DeletePrefixListParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)


class CreatePrefixListRuleParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
    prefix_list_rules: List[PrefixListRule] = Field(alias='prefixListRules', min_items=1, max_items=200)


class UpdatePrefixListRuleParam(PrefixListRule):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
    prefix_list_rule_id: StrictStr = Field(alias='prefixListRuleID', min_length=1)


class DeletePrefixListRuleParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
    prefix_list_rule_ids: StrictStr = Field(alias='prefixListRuleIDs', min_length=1)


class ClonePrefixListParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dest_region_id: StrictStr = Field(alias='destRegionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
    name: StrictStr
    limit: Optional[conint(strict=True, ge=1, le=200)]
    description: Optional[StrictStr]

    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)


class ListBindResourceParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    prefix_list_id: StrictStr = Field(alias='prefixListID', min_length=1)
