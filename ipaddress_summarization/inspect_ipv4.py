import ipaddress
import re
import json
import netaddr

def inspect_ipv4(ipAddress, subnets_prefix = 0, debug = {'status': False, 'level':0}):
    def ip_octant(x):
        if (x <= 8):
            return (8 - x)
        elif (x <= 16):
            return (16 - x)
        elif (x <= 24):
            return (24 - x)
        else:
            return (32 - x)

    def ip_increment(x):
        return pow(2,x)

    rc = re.compile(r"\s+") 
    rs = re.sub(rc, "/", ipAddress)
    data = ipaddress.ip_network(rs.strip() , strict=False)
    #     handles edge case prefixes length 0
    if (int(data.prefixlen) == 0):
            # print("Oops!  That was no valid number.  Try again...")
            return "Oops!  That was no valid number.  Try again..."
    results = {}
#     handles edge case prefixes lengths 31 and 32
    if (int(data.prefixlen) in [31,32]):
        results = {
            "network_address": str(data.network_address),
            "broadcast_address": str(data.broadcast_address),
            "prefix": data.prefixlen,
            "netmask": str(data.netmask),
            "host_range_begin": str(data.network_address),
            "host_range_end": str(data.broadcast_address),
            "hosts": len(list(data)),
            "hostmask": str(data.hostmask),
            "network_increment":ip_increment(ip_octant(data.prefixlen))
        }

    else:
        results = {
            "network_address": str(data.network_address),
            "broadcast_address": str(data.broadcast_address),
            "prefix": data.prefixlen,
            "netmask": str(data.netmask),
            "host_range_begin": str(data.network_address + 1),
            "host_range_end": str(data.broadcast_address - 1),
            "hosts": len(list(data)),
            "hostmask": str(data.hostmask),
            "network_increment":ip_increment(ip_octant(data.prefixlen))
        }
    

    if (subnets_prefix > 0):
        subnets = len(list(ipaddress.ip_network(rs).subnets(new_prefix=subnets_prefix)))
        results['subnets'] = {'subnets_prefix': subnets_prefix, 'subnets_count': subnets}
    if (debug['status']):
        print("network_address: ", data.network_address)
        print("broadcast_address: ", data.broadcast_address)
        print("prefix: ", data.prefixlen)
        print("netmask: ", data.netmask)
        print("host_range: ", data.network_address + 1, " - ", data.broadcast_address - 1)
        print("hosts: ", len(list(data)))
        print("hostmask: ", data.hostmask)
    return results