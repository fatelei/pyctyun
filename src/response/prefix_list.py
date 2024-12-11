from typing import Optional

from pydantic import BaseModel, Field

from .base import BaseResponse


class PrefixListRule(BaseModel):
    prefix_list_rule_id: str = Field(alias='prefixListRuleID')
    cidr: str
    description: str


class PrefixList(BaseModel):
    prefix_list_id: str = Field(alias='prefixListID')
    name: str
    limit: int
    address_type: str = Field(alias='addressType')
    description: str
    created_at: str = Field(alias='createdAt')
    updated_at: str = Field(alias='updatedAt')
    prefix_list_rules: list[PrefixListRule] = Field(alias='prefixListRules')


class Resource(BaseModel):
    resource_id: str = Field(alias='resourceID')
    resource_name: str = Field(alias='resourceName')
    resource_type: str = Field(alias='resourceType')
    
    
class DeletePrefixListRule(BaseModel):
    
    prefix_list_id: str = Field(alias='prefixListID')
    prefix_list_rule_id: str = Field(alias='prefixListRuleID')


class PrefixListIDResponse(BaseModel):
    prefix_list_id: str = Field(alias='prefixListID')


class ModifyPrefixListResponse(BaseResponse):
    return_obj: Optional[PrefixListIDResponse] = Field(alias='returnObj')


class ClonePrefixListResponse(BaseResponse):
    return_obj: Optional[PrefixListIDResponse] = Field(alias='returnObj')


class CreatePrefixListResponse(BaseResponse):
    return_obj: Optional[PrefixListIDResponse] = Field(alias='returnObj')


class DeletePrefixListResponse(BaseResponse):
    return_obj: Optional[PrefixListIDResponse] = Field(alias='returnObj')


class ListPrefixList(BaseModel):
    results: list[PrefixList]
    total_page: int = Field(alias='totalPage')
    current_count: int = Field(alias='currentCount')
    total_count: int = Field(alias='totalCount')


class ListPrefixResponse(BaseResponse):
    return_obj: Optional[ListPrefixList] = Field(alias='returnObj')


class ShowPrefixListResponse(BaseResponse):
    return_obj: Optional[PrefixList] = Field(alias='returnObj')


class ListResource(BaseModel):
    results: list[Resource]
    total_page: int = Field(alias='totalPage')
    current_count: int = Field(alias='currentCount')
    total_count: int = Field(alias='totalCount')


class ListResourceResponse(BaseResponse):
    return_obj: Optional[ListResource] = Field(alias='returnObj')
    
    
class DeletePrefixListRuleResponse(BaseResponse):
    return_obj: Optional[DeletePrefixListRule] = Field(alias='returnObj')


class UpdatePrefixListRuleResponse(BaseResponse):
    return_obj: Optional[DeletePrefixListRule] = Field(alias='returnObj')