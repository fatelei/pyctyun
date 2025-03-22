from typing import Optional, List

from pydantic import Field, field_validator, StrictStr

from src.rules.rule import check_description, BaseParamModel, check_ips, \
    check_name, PaginationGetParamModel, check_domain_name, check_ipv4_map_ipv6_addr


class CreateDhcpoptionSetsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    name: StrictStr
    domain_name: StrictStr = Field(alias='domainName', min_length=1)
    description: Optional[StrictStr]
    dns_list: List[StrictStr] = Field(alias='dnsList', min_items=1, max_items=4, min_length=1)
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)
    _check_domain_name = field_validator('domain_name')(check_domain_name)
    
    @field_validator("dns_list", allow_reuse=True)
    def check_dns_list(cls, v):
        check_ips(v)
        for i in v:
            check_ipv4_map_ipv6_addr(i)
        return v


class DeleteDhcpoptionSetsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dhcpoptionsets_id: StrictStr = Field(alias='dhcpOptionSetsID', min_length=1)


class UpdateDhcpoptionSetsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dhcpoptionsets_id: StrictStr = Field(alias='dhcpOptionSetsID', min_length=1)
    name: Optional[StrictStr]
    domain_name: Optional[StrictStr] = Field(alias='domainName', min_length=1)
    description: Optional[StrictStr]
    dns_list: Optional[List[StrictStr]] = Field(alias='dnsList', min_items=1, max_items=4, min_length=1)
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)
    _check_domain_name = field_validator('domain_name')(check_domain_name)
    
    @field_validator("dns_list", allow_reuse=True)
    def check_dns_list(cls, v):
        check_ips(v)
        for i in v:
            check_ipv4_map_ipv6_addr(i)
        return v


class QueryDhcpoptionSetsParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    query_content: Optional[StrictStr] = Field(alias='queryContent')


class ShowDhcpoptionSetsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dhcpoptionsets_id: StrictStr = Field(alias='dhcpOptionSetsID', min_length=1)


class DhcpoptionWithVpcParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dhcpoptionsets_id: StrictStr = Field(alias='dhcpOptionSetsID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)


class DhcpoptionListVpcParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    dhcpoptionsets_id: StrictStr = Field(alias='dhcpOptionSetsID', min_length=1)


class DhcpoptionListUnbindVpcParam(PaginationGetParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
