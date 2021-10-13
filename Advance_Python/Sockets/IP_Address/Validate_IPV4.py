# Python program to implement validate the IPV4 address

import ipaddress

# valid IPV4 address
print(ipaddress.ip_address(u'192.168.0.255'))

# invalid IPV4 address
print(ipaddress.ip_address(u'192.168.0.256'))