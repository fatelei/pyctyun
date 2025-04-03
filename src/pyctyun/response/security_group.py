from pydantic import BaseModel, Field

from .base import BaseResponse


class CreateSgIDResponse(BaseModel):
    security_group_id: str = Field(alias="securityGroupID")


class SecurityGroupRule(BaseModel):
    direction: str
    priority: int
    ethertype: str
    protocol: str
    range: str
    dest_cidr_ip: str = Field(alias="destCidrIp")
    description: str
    create_time: str = Field(alias="createTime")
    id: str
    security_group_id: str = Field(alias="securityGroupID")
    action: str
    origin: str
    remote_securityGroup_id: str = Field(alias="remoteSecurityGroupID")
    prefix_list_id: str = Field(alias="prefixListID")


class CreateSecurityGroupResponse(BaseResponse):
    return_obj: CreateSgIDResponse = Field(alias="returnObj")


class ShowSgRuleResponse(BaseResponse):
    return_obj: SecurityGroupRule = Field(alias="returnObj")


class SecurityGroup(BaseModel):
    security_group_name: str = Field(alias="securityGroupName")
    id: str
    vm_num: int = Field(alias="vmNum")
    origin: str
    vpc_name: str = Field(alias="vpcName")
    vpc_id: str = Field(alias="vpcID")
    creation_time: str = Field(alias="creationTime")
    description: str
    security_group_rule_list: list[SecurityGroupRule] = Field(alias="securityGroupRuleList")


class NewListSg(BaseModel):
    security_groups: list[SecurityGroup] = Field(alias="securityGroups")
    total_count: int = Field(alias="totalCount")
    current_count: int = Field(alias="currentCount")
    total_page: int = Field(alias="totalPage")


class NewListSgResponse(BaseResponse):
    return_obj: NewListSg = Field(alias="returnObj")


class ListSgResponse(BaseResponse):
    total_count: int = Field(alias="totalCount")
    current_count: int = Field(alias="currentCount")
    total_page: int = Field(alias="totalPage")
    return_obj: list[SecurityGroup] = Field(alias="returnObj")


class ShowSgResponse(BaseResponse):
    return_obj: SecurityGroup = Field(alias="returnObj")


class AsssociateVm(BaseModel):
    instance_id: str = Field(alias="instanceID")
    instance_name: str = Field(alias="instanceName")
    instance_type: str = Field(alias="instanceType")
    instance_state: str = Field(alias="instanceState")
    private_ip: str = Field(alias="privateIp")
    private_ipv6: str = Field(alias="privateIpv6")


class ListSgAssociateObj(BaseModel):
    total_count: int = Field(alias="totalCount")
    current_count: int = Field(alias="currentCount")
    total_page: int = Field(alias="totalPage")
    results: list[AsssociateVm]


class ListSgAssociateVmResponse(BaseResponse):
    return_obj: ListSgAssociateObj = Field(alias="returnObj")
