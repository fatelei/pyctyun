from typing import Optional

from pydantic import Field, field_validator, StrictBool, StrictStr

from src.rules.rule import check_name, check_description, check_cidr, check_ips, check_ip, check_subnet_type, \
    BaseParamModel, PaginationGetParamModel


class CreateSubnetParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)
    name: StrictStr = Field(max_length=31, min_length=1)
    description: StrictStr = Field('', min_length=0, max_length=128)
    cidr: StrictStr = Field(alias='CIDR', min_length=1)
    enable_ipv6: Optional[StrictBool] = Field(alias='enableIpv6')
    dns_list: Optional[list[str]] = Field(alias='dnsList', max_items=4)
    subnet_gateway_ip: Optional[str] = Field(alias='subnetGatewayIP')
    subnet_type: StrictStr = Field("common", alias='subnetType')
    project_id: Optional[StrictStr] = Field('0', alias='projectID')
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)
    _check_cidr = field_validator('cidr')(check_cidr)
    _check_dns_list = field_validator('dns_list')(check_ips)
    _check_subnet_gateway_ip = field_validator('subnet_gateway_ip')(check_ip)
    _check_subnet_type = field_validator('subnet_type')(check_subnet_type)


class DeleteSubnetParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)


class UpdateSubnetParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    name: Optional[StrictStr]
    dns_list: Optional[list[str]] = Field(alias='dnsList', max_items=4)
    description: Optional[StrictStr]
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)
    _check_dns_list = field_validator('dns_list')(check_ips)


class SubnetReplaceRouteTableParam(BaseParamModel):
    client_token: Optional[StrictStr] = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    route_table_id: StrictStr = Field(alias='routeTableID', min_length=1)


class SubnetDisassociateRouteTableParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)


class SubnetCreateACLParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    project_id: StrictStr = Field('0', alias='projectID')
    name: StrictStr = Field(min_length=1)
    description: Optional[StrictStr]
    
    _check_name = field_validator('name')(check_name)
    _check_description = field_validator('description')(check_description)


class SubnetEnableIPv6Param(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)


class SubnetDisassociateACLParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    acl_id: StrictStr = Field(alias="aclID", min_length=1)


class SubnetReplaceACLParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    acl_id: StrictStr = Field(alias="aclID", min_length=1)


class UpdateSubnetIPv6StatusParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    enable_ipv6: StrictBool = Field(alias="enableIpv6")


class ListSubnetsParam(PaginationGetParamModel):
    region_id: Optional[str] = Field(alias='regionID')
    subnet_id: Optional[str] = Field(alias='subnetID')
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)


class ShowSubnetParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)


class CheckIpAvaliableParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    subnet_id: StrictStr = Field(alias='subnetID', min_length=1)
    ip: StrictStr = Field(alias='fixedIP', min_length=1)
    
    _check_ip = field_validator('ip')(check_ip)
