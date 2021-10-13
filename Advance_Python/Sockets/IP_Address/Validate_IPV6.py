# Python program to implement validation of IPV6 address

import ipaddress

# valid IPV6 address
print(ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))

# invalid IPV6 address
print(ipaddress.ip_address(u'FFFF:10000:2:FDE:257:0:2FAE:112D'))