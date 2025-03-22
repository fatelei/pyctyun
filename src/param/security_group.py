from typing import List, Optional

from pydantic import Field, StrictBool, StrictStr, StrictInt, conint, field_validator

from src.rules.rule import check_description, BaseParamModel, check_name, PaginationGetParamModel, check_uuid, \
    check_uuids



class CreateSecurityGroupParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    project_id: Optional[StrictStr] = Field('0', alias='projectID')
    vpc_id: StrictStr = Field(alias='vpcID', min_length=1)
    name: StrictStr
    description: Optional[StrictStr]
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)


class RemoveSecurityGroupParam(BaseParamModel):
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    az_name: StrictStr = Field('', alias='azName')
    project_id: StrictStr = Field('0', alias='projectID')
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)


class UnbindSecurityGroupParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    instance_id: StrictStr = Field(alias='instanceID', min_length=1)
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)


class BindSecurityGroupParam(BaseParamModel):
    network_interface_id: StrictStr = Field('', alias='networkInterfaceID')
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    instance_id: StrictStr = Field(alias='instanceID', min_length=1)
    action: StrictStr
    
    @field_validator('action')
    def check_action(cls, value):
        if value != 'joinSecurityGroup':
            raise ValueError('action must be joinSecurityGroup')
        return value


class BatchBindSecurityGroupParam(BaseParamModel):
    network_interface_id: Optional[StrictStr] = Field(alias='networkInterfaceID')
    security_group_ids: list[str] = Field(alias='securityGroupIDs', min_items=1, max_items=10)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    instance_id: StrictStr = Field(alias='instanceID', min_length=1)
    action: StrictStr
    
    _check_sg_ids = field_validator('security_group_ids')(check_uuids)
    _check_network_interface_id = field_validator('network_interface_id')(check_uuid)
    
    @field_validator('action')
    def check_action(cls, value):
        if value != 'joinSecurityGroup':
            raise ValueError('action must be joinSecurityGroup')
        return value


class BatchUnBindSecurityGroupParam(BaseParamModel):
    network_interface_id: Optional[StrictStr] = Field(alias='networkInterfaceID')
    security_group_ids: list[str] = Field(alias='securityGroupIDs', min_items=1, max_items=10)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    instance_id: StrictStr = Field(alias='instanceID', min_length=1)
    action: StrictStr
    
    _check_sg_ids = field_validator('security_group_ids')(check_uuids)
    _check_network_interface_id = field_validator('network_interface_id')(check_uuid)
    
    @field_validator('action')
    def check_action(cls, value):
        if value != 'leaveSecurityGroup':
            raise ValueError('action must be leaveSecurityGroup')
        return value


class GetSecurityGroupParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    sg_rule_direction: StrictStr = Field('all', alias='direction')
    
    @field_validator('sg_rule_direction')
    def check_sg_rule_direction(cls, value):
        if value not in ('all', 'egress', 'ingress'):
            raise ValueError('only support all / egress / ingress')
        return value


class UpdateSecurityGroupParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    name: Optional[str] = Field('', max_length=32, min_length=1)
    description: Optional[str] = Field('', min_length=0, max_length=128)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    enabled: Optional[StrictBool] = None
    
    _check_description = field_validator('description')(check_description)
    _check_name = field_validator('name')(check_name)


class ListSecurityGroupsParam(PaginationGetParamModel):
    vpc_id: StrictStr = Field('', alias='vpcID')
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    instance_id: StrictStr = Field('', alias='instanceID')
    query_content: StrictStr = Field('', alias='queryContent')


class RemoveSecurityGroupRuleParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    security_group_rule_id: StrictStr = Field(alias='securityGroupRuleID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)


class BatchRemoveSecurityGroupRuleParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    security_group_rule_ids: list[StrictStr] = Field(alias='securityGroupRuleIDs', max_items=10, min_items=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class SecurityRule(BaseParamModel):
    direction: StrictStr
    action: StrictStr
    priority: conint(strict=True, ge=1, le=100) = 100
    protocol: StrictStr
    ethertype: StrictStr
    remote_type: StrictInt = Field(0, alias="remoteType")
    remote_ip_prefix: StrictStr = Field('', alias='destCidrIp')
    description: Optional[StrictStr]
    range: StrictStr = Field('')
    remote_security_group_id: Optional[StrictStr] = Field(alias="remoteSecurityGroupID")
    prefixlist_id: Optional[StrictStr] = Field(alias="prefixListID")
    
    _check_description = field_validator('description')(check_description)
    
    @field_validator("remote_type")
    def check_remote_type(cls, v):
        if v is not None and v not in (0, 1, 2):
            raise ValueError("remoteType only support 0, 1, 2")
        return v
    
    @field_validator('direction')
    def check_direction(cls, value: StrictStr):
        if value.lower() not in ('egress', 'ingress'):
            raise ValueError('only support egress / ingress')
        return value.lower()
    
    @field_validator('action')
    def check_action(cls, value: StrictStr):
        tmp = value.lower()
        if tmp not in ('accept', 'drop'):
            raise ValueError('only support accept / drop')
        return tmp
    
    @field_validator('ethertype')
    def check_ethertype(cls, value: StrictStr):
        if value.lower() not in ('ipv4', 'ipv6'):
            raise ValueError('only support ipv4 / ipv6')
        return value.lower()
    
    @field_validator('protocol')
    def check_protocol(cls, value: StrictStr):
        if value.lower() not in ('any', 'tcp', 'udp', 'icmp', 'icmp6'):
            raise ValueError('only support any / tcp / udp / icmp / icmp6')
        return value.lower()
    
    @field_validator('range')
    def check_range(cls, v: StrictStr, values, **kwargs):
        if 'protocol' not in values:
            return v
        
        if values['protocol'].lower() not in ('tcp', 'udp'):
            return ''
        else:
            if not v:
                raise ValueError("when protocol is tcp / udp，range is required")
            
            if v.startswith('-'):
                raise ValueError('range could not start with -')
            tmp = v.split('-')
            if len(tmp) == 2:
                if not tmp[0].isdigit() or not tmp[1].isdigit():
                    raise ValueError('range format support number-number')
                
                if int(tmp[0]) > int(tmp[1]):
                    raise ValueError('end port number must be bigger than start port number')
                
                if int(tmp[0]) < 1 or int(tmp[1]) > 65535:
                    raise ValueError("when protocol is TCP / UDP, port number must be 1 - 65535")
            else:
                if not tmp[0].isdigit():
                    raise ValueError('port number is not digit')
                
                if not 1 <= int(tmp[0]) <= 65535:
                    raise ValueError("when protocol is TCP / UDP, port number must be 1 - 65535")
            return v


class PreCreateCheckParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    security_group_rule: SecurityRule = Field(alias='securityGroupRule')


class CreateSecurityGroupRuleParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    security_group_rules: List[SecurityRule] = Field(alias='securityGroupRules', min_items=1)


class ModifySecurityGroupRuleParam(BaseParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    security_group_rule_id: StrictStr = Field(alias='securityGroupRuleID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    description: Optional[StrictStr]
    action: Optional[StrictStr]
    priority: Optional[conint(strict=True, ge=1, le=100)]
    protocol: Optional[StrictStr]
    remote_type: StrictInt = Field(0, alias="remoteType")
    remote_ip_prefix: Optional[StrictStr] = Field('', alias='destCidrIp')
    remote_security_group_id: Optional[StrictStr] = Field(alias="remoteSecurityGroupID")
    prefixlist_id: Optional[StrictStr] = Field(alias="prefixListID")
    
    _check_description = field_validator('description')(check_description)
    
    @field_validator('action')
    def check_action(cls, value: StrictStr):
        if not value:
            return value
        tmp = value.lower()
        if tmp not in ('accept', 'drop'):
            raise ValueError('only support accept / drop')
        return tmp
    
    @field_validator('protocol')
    def check_protocol(cls, value: StrictStr):
        if not value:
            return value
        if value.lower() not in ('any', 'tcp', 'udp', 'icmp', 'icmp6'):
            raise ValueError('only support any / tcp / udp / icmp / icmp6')
        return value.lower()
    
    @field_validator("remote_type")
    def check_remote_type(cls, v):
        if v is not None and v not in (0, 1, 2):
            raise ValueError("remoteType only support 0, 1, 2")
        return v


class BatchAttachSecurityGroupPortsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    port_ids: list[str] = Field(alias='portIDs', min_items=1, max_items=10)


class BatchDetachSecurityGroupPortsParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)
    client_token: StrictStr = Field(alias='clientToken', min_length=1, max_length=64)
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    port_ids: list[str] = Field(alias='portIDs', min_items=1, max_items=10)


class GetSecurityGroupAssociateVmParam(PaginationGetParamModel):
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class ShowSecurityGroupRuleParam(PaginationGetParamModel):
    security_group_rule_id: StrictStr = Field(alias='securityGroupRuleID', min_length=1)
    security_group_id: StrictStr = Field(alias='securityGroupID', min_length=1)
    region_id: StrictStr = Field(alias='regionID', min_length=1)
