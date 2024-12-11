import ipaddress
import re
from typing import List, Optional

from email_validator import EmailNotValidError, EmailSyntaxError, validate_email
from pydantic import BaseModel, conint, Field, StrictStr

name_regex = re.compile(
    r'^([a-zA-Z]|[\u4e00-\u9fff])([a-zA-Z0-9_\-]|[\u4e00-\u9fff]){1,31}$')
vpce_service_name_regex = re.compile(
    r'^(([a-zA-Z0-9]|[\u4e00-\u9fff])([a-zA-Z0-9_\-]|[[\u4e00-\u9fff]]){0,63})(\.([a-zA-Z0-9]|[[\u4e00-\u9fff]])([a-zA-Z0-9_\-]|[[\u4e00-\u9fff]]){0,63})*$')
desc_regex = re.compile(
    r"^([~!@#$%^&*()_\-+= <>?:\"{}|,.\/;'[\]·~！@#￥%……&*（） ——\-+={}|《》？：“”【】、；‘'，。、]|[a-zA-Z0-9]|[\u4e00-\u9fff]){0,128}$")
uuid_regex = re.compile(r'^[a-z0-9][a-z0-9-]{1,35}$')
vpcx_device_regex = re.compile(r'^[a-zA-Z0-9_-]{1,36}$')
email_rule = re.compile(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$")
dns_name_regex = re.compile(
    r'^[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(?<!-)(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+(?<!-)$')
dns_name_wild_regex = re.compile(
    r'^(\*)(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$')
mx_value_regex = re.compile(
    r'^[0-9]{1,5}\s[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})*$')
txt_value_regex = re.compile(
    r'^(\"[a-zA-Z0-9~\!\@\#\$\%\^\&\*\(\)\_\+\-\=\{\}\|\[\]\:\;\'\,\.\/\<\>\?\s]{0,255}\")(\s\"[a-zA-Z0-9\~\!\@\#\$\%\^\&\*\(\)\_\+\-\=\{\}\|\[\]\:\;\'\,\.\/\<\>\?\s]{0,255}\")*$')

host_record_regex = re.compile(
    r'^(\*\.)?[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(?<!-)(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})*(?<!-)$')
domain_name_regex = re.compile(
    r'^([a-zA-Z0-9][a-zA-Z0-9\-]{0,62})(\.[a-zA-Z0-9][a-zA-Z0-9\-]{0,62})+$')
elb_http_expected_codes_regex = re.compile(
    r'^(\d{3}(\s*,\s*\d{3})*)$|^(\d{3}-\d{3})$')
srv_regex = re.compile(
    r'^[0-9]{1,5}\s[0-9]{1,5}\s[0-9]{1,5}\s[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})*$')
http_url_path_regex = re.compile(r'^(/[0-9a-zA-Z\-_./=]*)?$')
mac_regex = re.compile(
    r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$|^([0-9A-Fa-f]{4}\.){2}([0-9A-Fa-f]{4})$')


class BaseParamModel(BaseModel):
    class Config:
        str_strip_whitespace = True


class GetQuotaParam(BaseParamModel):
    region_id: StrictStr = Field(alias='regionID', min_length=1)


class PaginationGetParamModel(BaseParamModel):
    page_number: Optional[conint(ge=1)] = Field(1, alias='pageNumber')
    page_size: conint(ge=1, le=50) = Field(10, alias='pageSize')


class PaginationPostParamModel(BaseParamModel):
    page_number: Optional[conint(strict=True, ge=1)] = Field(
        alias='pageNumber')
    page_size: conint(strict=True, ge=1, le=50) = Field(10, alias='pageSize')


def check_dns_name(name: str | None) -> str | None:
    if name is not None:
        if len(name) == 0:
            return name
        
        if not 1 <= len(name) <= 254:
            raise ValueError("length should be 1 - 254")
        
        ary = name.split('.')
        for i in ary:
            if not 1 <= len(i) <= 63:
                raise ValueError(
                    "each part of domain name length should be 1 - 63")
        
        if not dns_name_regex.match(name) and not dns_name_wild_regex.match(name):
            raise ValueError(
                "must contain dot, must not start with or end with hyphen, support letter, digit, hyphen, dot")
    return name


def check_ptr(name: str | None) -> str | None:
    if name is not None:
        match = dns_name_regex.match(name)
        if not match or len(name) > 254:
            raise ValueError(
                f"Zone record PTR type value {name} was wrong format")
    return name


def check_srv(name: str | None) -> str | None:
    if name is not None:
        if not srv_regex.match(name):
            raise ValueError(
                f'Zone record SRV type value {name} wrong format.')
        
        tmp_ary = name.split(" ")
        if len(tmp_ary) != 4:
            raise ValueError(
                f'Zone record SRV type value {name} wrong format.')
        
        priority, weight, port, domain_name = tmp_ary
        if not priority.isdigit() or not 1 <= int(priority) <= 65535:
            raise ValueError(
                'Zone record SRV type value priority must be [0, 65535] range.')
        
        if not weight.isdigit() or not 1 <= int(weight) <= 65535:
            raise ValueError(
                'Zone record SRV type value weight must be [0, 65535] range.')
        
        if not port.isdigit() or not 1 <= int(port) <= 65535:
            raise ValueError(
                'Zone record SRV type value port must be [0, 65535] range.')
        
        is_match = dns_name_regex.match(domain_name)
        if not is_match or len(domain_name) > 254:
            raise ValueError(
                f"Zone record SRV type value {domain_name} was wrong format")
    return name


def check_aaaa(name: str | None) -> str | None:
    if name is not None:
        tmp = ipaddress.ip_address(name)
        if tmp.version != 6:
            raise ValueError(
                'Zone record AAAA type value must be IPv6 format.')
    return name


def check_uuid(value: str) -> str:
    if value and not uuid_regex.match(value):
        raise ValueError(f"{value} format error")
    return value


def check_uuids(value: list[str]) -> list[str] | None:
    if value is not None:
        for i in value:
            check_uuid(i)
    return value


def check_email(email: str) -> str:
    if email is not None:
        try:
            validate_email(email, check_deliverability=False)
        except (EmailSyntaxError, EmailNotValidError):
            raise ValueError(f"{email} format error")
    return email


def check_vpce_service_name(name: str):
    if name is not None:
        if name.startswith('http:') or name.startswith('https:'):
            raise ValueError("should not start with http: or https:")
        if not vpce_service_name_regex.match(name):
            raise ValueError(
                "format error：only support en letter、chinese、-、_、digits, and should starts with letter / chinese")
    return name


def check_name(name: str) -> str:
    if name is not None:
        if name.startswith('http:') or name.startswith('https:'):
            raise ValueError("should not start with http: or https:")
        if not 2 <= len(name) <= 32:
            raise ValueError("length should be  2 - 32")
        if not name_regex.match(name):
            raise ValueError(
                "format error：only support en letter、chinese、-、_、digits, and should starts with letter / chinese")
    return name


def check_pay_voucher_price(price: str) -> str:
    try:
        tmp = float(price)
        if tmp < 0:
            raise ValueError("must bigger than 0")
        if "." in price:
            part = price.split(".")[1]
            if len(part) > 2:
                raise ValueError("two decimal places")
        return price
    except ValueError:
        raise


def check_oa_type(oa_type: str) -> str:
    if oa_type is not None:
        if oa_type not in ('tcp_option', 'proxy_protocol', 'close'):
            raise ValueError(
                "only support close / tcp_option / proxy_protocol")
    return oa_type


def check_host_record(host_record, v):
    if host_record != "" and host_record != '*':
        if len(v) > 256:
            raise ValueError("length should less than equal to 256")
        
        if not host_record_regex.match(v):
            raise ValueError(f'zone record host record {v} was wrong format')


def check_record_type(value: str) -> str:
    if value is not None:
        if value.upper() not in ('A', 'AAAA', 'TXT', 'CNAME', 'MX'):
            raise ValueError("only support A / AAAA / TXT / CNAME / MX")
    return value


def check_certificate_type(certificate_type: str) -> str:
    if certificate_type is not None:
        if certificate_type not in ('Server', 'Ca'):
            raise ValueError('only support Server / Ca')
    return certificate_type


def check_elb_resource_type(resource_type: str) -> str:
    if resource_type is not None:
        if resource_type not in ('external', 'internal'):
            raise ValueError('only support external / internal')
    return resource_type


def check_proxy_pattern(proxy_pattern: str) -> str:
    if proxy_pattern is not None:
        if proxy_pattern.lower() not in ('zone', 'record'):
            raise ValueError('only support zone / record')
    return proxy_pattern


def check_domain_name(v: str) -> str:
    if v is not None:
        if len(v) > 255:
            raise ValueError('length shoud be less than 255')
        if not domain_name_regex.match(v):
            raise ValueError(
                "format error：Invalid domain name")
    return v


def check_elb_http_expected_codes(v: str) -> str:
    if v is not None:
        if len(v) > 64:
            raise ValueError('length shoud be less than 64')
        if not elb_http_expected_codes_regex.match(v):
            raise ValueError(
                "format error：Invalid httpExpectedCodes")
    return v


def check_description(description: str) -> str:
    if description is not None:
        if description.startswith('http:') or description.startswith('https:'):
            raise ValueError("should not start with http: or https:")
        if len(description) > 128:
            raise ValueError("length should be  0 - 128")
        if not desc_regex.match(description):
            raise ValueError(
                "format error：only support en letter、chinese、digits, ~!@#$%^&*()_\\-+= <>?:\"{}|,.\/;'[\]·~！@#￥%……&*（） ——\-+={}|《》？：“”【】、；‘'，。、")
    return description


def check_port_range(value: str) -> str:
    if value is not None:
        value_ary = value.split(":")
        if len(value_ary) == 1:
            if not value_ary[0].isdigit():
                raise ValueError("is not a number")
            check_port(int(value_ary[0]))
        elif len(value_ary) == 2:
            for i in value_ary:
                if not i.isdigit():
                    raise ValueError("is not a number")
                check_port(int(i))
            
            if int(value_ary[0]) > int(value_ary[1]):
                raise ValueError(
                    "port_start must be less than or equal to port_end")
        else:
            raise ValueError("invalid port range")
    return value


def check_port(port: int) -> int:
    if not 1 <= port <= 65535:
        raise ValueError("port number is 1 - 65535")
    return port


def check_target_group_algorithm(algorithm: str) -> str | None:
    if algorithm is not None and algorithm not in ('rr', 'wrr', 'lc', 'sh'):
        raise ValueError('only support rr / wrr / lc / sh')
    return algorithm


def check_sticky_session_mode(mode: str) -> str:
    # elb server not support source_ip
    if mode and mode.lower() not in ('close', 'insert', 'rewrite'):
        raise ValueError('only support CLOSE / INSERT / REWRITE')
    return mode


def check_cookie_expire(v: int | None, values):
    if 'session_sticky_mode' in values and values['session_sticky_mode'] == 'INSERT' and not v:
        raise ValueError('when sessionStictyMode is INSERT，field required')
    return v


def check_source_ip_timeout(v: int | None, values):
    if 'session_sticky_mode' in values and values['session_sticky_mode'] == 'SOURCE_IP' and not v:
        raise ValueError('when sessionStictyMode is SOURCE_IP，field required')
    return v


def check_rewrite_cookie_name(v: int | None, values):
    if 'session_sticky_mode' in values and values['session_sticky_mode'] == 'REWRITE' and not v:
        raise ValueError('when sessionStictyMode is REWRITE，field required')
    return v


def check_record_type_and_value(record_type, v):
    record_type = record_type.upper()
    if record_type == 'CNAME':
        if len(v) > 1:
            raise ValueError("when type is CNAME, only one value is supported")
        check_dns_name(v[0])
    elif record_type == 'A':
        for i in v:
            try:
                a = ipaddress.ip_address(i)
                if a.version != 4:
                    raise ValueError("invalid ip address")
            except ValueError:
                raise ValueError("invalid ip address")
    elif record_type == 'AAAA':
        for i in v:
            check_ipv6(i)
    elif record_type == 'MX':
        for i in v:
            check_mx(i)
    elif record_type == 'TXT':
        data = []
        for i in v:
            check_txt(i)
            data.append(f"\"{i}\"")
        return data
    return v


def check_ip(ip: str) -> str:
    if ip is not None:
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            raise ValueError("invalid ip address")
    return ip


def check_mac(mac: str) -> str:
    if mac is not None:
        if not mac_regex.match(mac):
            raise ValueError("invalid MAC address")
    return mac


def check_mx(v: str) -> str:
    if not mx_value_regex.match(v):
        raise ValueError(f"zone record MX type value [{v}] was wrong format.")
    
    ary = v.split(" ")
    if len(ary) != 2:
        raise ValueError(f'zone record MX type value [{v}] was wrong format')
    priority, domain_name = ary
    if not priority.isdigit():
        raise ValueError('zone record MX type value was wrong format')
    
    if not 0 <= int(priority) <= 65535:
        raise ValueError(
            'zone record MX type value priority must be [0, 65535] range')
    
    check_dns_name(domain_name)
    return v


def check_txt(v: str) -> str:
    if not txt_value_regex.match(f"\"{v}\""):
        raise ValueError(f"zone record TXT type value [{v}] was wrong format")
    if len(v) > 4096:
        raise ValueError(
            f'zone record TXT type value [{v}] length should not greater than 4096')
    
    return v


def check_ipv6(ip: str) -> str:
    if ip is not None:
        try:
            a = ipaddress.ip_address(ip)
            if a.version != 6:
                raise ValueError("invalid ipv6 address")
        except ValueError:
            raise ValueError("invalid ipv6 address")
    return ip


def check_ipv6s(data: list[str]) -> list[str]:
    if not data:
        return []
    rst = set()
    for i in data:
        rst.add(check_ipv6(i))
    return list(rst)


def check_ips(data: list[str]) -> list[str]:
    if not data:
        return []
    
    rst = set()
    for i in data:
        rst.add(check_ip(i))
    return list(rst)


def check_subnet_type(subnet_type: str) -> str:
    if subnet_type not in ('common', 'cbm'):
        raise ValueError('only support common / cbm')
    return subnet_type


def check_cidr(cidr: str) -> str:
    if cidr is not None:
        try:
            ipaddress.ip_network(cidr)
        except ValueError:
            raise
    return cidr


def check_vpc_cidr(cidr: str) -> str:
    if cidr is not None:
        try:
            a = ipaddress.ip_network(cidr)
        except ValueError:
            raise
        
        if a.prefixlen > 28:
            raise ValueError('cidr prefix should be less than 28')
    return cidr


def check_cidrs(cidrs: List[str]) -> List[str]:
    if not cidrs:
        return []
    data = set()
    for cidr in cidrs:
        data.add(check_cidr(cidr))
    return list(data)


def check_mirror_filter_rule_port(port: str) -> str:
    if port is not None:
        if port == '-':
            return port
        else:
            ary = port.split('/')
            if len(ary) != 2:
                raise ValueError('format error')
            if not ary[0].isdigit() or not 1 <= int(ary[0]) <= 65535:
                raise ValueError('format error')
            
            if not ary[1].isdigit() or not 1 <= int(ary[1]) <= 65535:
                raise ValueError('format error')
    return port


def check_target_instance_type(v: str) -> str:
    if v.lower() not in ('vm', 'bm', 'ip'):
        raise ValueError('only support VM / BM / IP')
    return v


def check_private_nat_spec(spec: str) -> str:
    if spec not in ('small', 'medium', 'large', 'xlarge'):
        raise ValueError('spec must be one of small/medium/large/xlarge')
    return spec


def check_cycle_count(v, values, **kwargs):
    if 'cycle_type' not in values:
        return v
    
    cycle_type = values['cycle_type'].lower()
    match cycle_type:
        case 'on_demand':
            return v
        case 'year':
            if not v:
                raise ValueError(
                    'when cycleType is YEAR, cycleCount field required')
            if not 1 <= v <= 3:
                raise ValueError(
                    'when cycleType is YEAR, cycleCount should be range  1 - 3')
        case 'month':
            if not v:
                raise ValueError(
                    'when cycleType is MONTH, cycleCount field required')
            if not 1 <= v <= 11:
                raise ValueError(
                    'when cycleType is MONTH, cycleCount should be range  1 - 11')
        case _:
            return v


def check_ipv4_map_ipv6_cidr(v):
    if v.startswith("::ffff:") or v.startswith("0:0:0:0:0:ffff:"):
        ipv6_network = ipaddress.IPv6Network(v)
        ipv6_address = ipaddress.IPv6Address(ipv6_network.network_address.packed)
        if ipv6_address.ipv4_mapped:
            raise ValueError("ipv4 map 1pv6 is not allowed")
    return v


def check_ipv4_map_ipv6_addr(v):
    try:
        if v.startswith("::ffff:") or v.startswith("0:0:0:0:0:ffff:"):
            ipv6 = ipaddress.IPv6Address(v)
            if ipv6.ipv4_mapped:
                raise ValueError("ipv4 map 1pv6 is not allowed")
    except ipaddress.AddressValueError:
        pass
    return v
