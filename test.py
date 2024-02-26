import os, ipaddress

version = "ipv4"

def is_ip_in_cidr(ip, cidr):
    ip_obj = ipaddress.ip_address(ip)
    network = ipaddress.ip_network(cidr)
    return ip_obj in network


d = {}
if __name__ == "__main__":
    for x in os.listdir("./provider"):
        if x.endswith(version + ".txt"):
            data = open("./provider/" + x,'r').read().split('\n')
            name = x.split('-')[0]
            d[name] = data

urls = open('url.txt','r').read().split('\n')

for url in urls:
    found = False
    for key,value in d.items():
        for v in value:
            if is_ip_in_cidr(url, v):
                found = True
                print(url, key)
                break
    if not found:
        print(url, 'none')


