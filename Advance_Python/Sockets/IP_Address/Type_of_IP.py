# Python program to implement types of IP address

import ipaddress

print(type(ipaddress.ip_address(u'192.168.0.255')))

print(type(ipaddress.ip_address(u'2001:db8::')))

print(ipaddress.ip_address(u'192.168.0.255').reverse_pointer)

print(ipaddress.ip_network(u'192.168.0.0/28'))