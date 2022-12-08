def ipv4_from_inverse_mask(data:list):
    result = []
    for x in data:
        ip = [0 if int(x) == 1 else 1 for x in x]
        # resturns ipv4 base 10 list, might be worth it in the future
        # ip = str(ip_address(int(''.join(map(str, ip)), 2)))
        result.append(ip)
    return result