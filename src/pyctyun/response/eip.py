from typing import List, Optional

from pydantic import BaseModel, Field

from .base import BaseResponse


class Eip(BaseModel):
    id: str = Field(alias="ID")
    name: str
    eip_address: str = Field(alias="eipAddress")
    association_id: str = Field("", alias="associationID")
    association_type: Optional[str] = Field(None, alias="associationType")
    private_ip_address: Optional[str] = Field(None, alias="privateIpAddress")
    bandwidth: int
    bandwidth_id: str = Field("", alias="bandwidthID")
    bandwidth_type: str = Field(alias="bandwidthType")
    status: str
    tags: str
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    expired_at: Optional[str] = Field(None, alias="expiredAt")


class ListEip(BaseModel):
    eips: List[Eip]


class NewListEip(BaseModel):
    eips: List[Eip]
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')


class NewListEipResponse(BaseResponse):
    return_obj: NewListEip = Field(alias='returnObj')


class ListEipResponse(BaseResponse):
    return_obj: ListEip = Field(alias='returnObj')
    total_count: int = Field(alias='totalCount')
    current_count: int = Field(alias='currentCount')
    total_page: int = Field(alias='totalPage')
