import ipaddress

def ipaddress_is_subnet(a,b):
    networkA = ipaddress.ip_network(a,strict=False)
    networkB = ipaddress.ip_network(b,strict=False)
    return networkB.subnet_of(networkA)
