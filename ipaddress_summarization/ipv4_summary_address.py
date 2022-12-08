from ipaddress import IPv4Network, ip_network,ip_address
from netaddr import IPAddress, cidr_merge
import pandas as pd
from dataprep.clean import clean_ip
import pprint as pp
import numpy as np


def ipv4_summary_address(data):

    def make_subnet_mask(mask_bits):
        return [0 if x >= mask_bits else 1 for x in list(range(32))]
    def ip_format(ip):
        ip = ''.join(map(str, ip))
        return str(ip_address(int(ip, 2)))
    def common_bit(x):
        x = np.array(x)
        for index in range(32):
            # print(len(set(d[:,index])) <= 1)
            # super cool way to perform bindary anding against a two dimentional list
            if ((len(set(x[:,index])) <= 1) != True):
                # print(len(set(d[:,index])) <= 1, index)
                print(make_subnet_mask(index), ip_format(make_subnet_mask(index)), f"/{index}")
                return {
                    "network_bits":index,
                    "mask_binary":[0 if x > index else 1 for x in list(range(32))],
                    "mask": ip_format([0 if x > index else 1 for x in list(range(32))])
                }
        return True
    new_list = {
        "base2":[],
        "base10":[],
        "summary": {}
    }
    list_length = len(data)
    last_common_bit = None
    b_result = []
    [print(x, ip_format(x)) for x in data]
    new_list["base2"] = data
    new_list["base10"] = [ip_format(x) for x in data]
    new_list["summary"] = common_bit(new_list["base2"])
    # print(list(a and b for a,b in zip(x,y)),ip_format(y))
    # super cool way to perform bindary anding against two list
    # print(list(a and b for a,b in zip([1010],[1010])))
    print("\n")
    return new_list