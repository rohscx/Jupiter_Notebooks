from ipaddress import ip_address

def ipv4_from_base_2(data:list):
    ip = [''.join(map(str, x)) for x in data]
    return [str(ip_address(int(x, 2))) for x in ip]