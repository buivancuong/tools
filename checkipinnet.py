import ipaddress
import sys

ip = str(sys.argv[1])
subnet = str(sys.argv[2])
if ipaddress.ip_address(ip) in ipaddress.ip_network(subnet): print("in")
else: print("out")