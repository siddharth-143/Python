"""
    Python program to check hostname and ipaddress.
"""

import socket

def get_hostname_IP():
    hostname = input("Please enter a website addresss(URL) : ")
    try:
        print(f"Hostname : {hostname}")
        print(f"IP : {socket.gethostbyname(hostname)}")
    except socket.gaierror as error:
        print(f"Invalid Hostname, error raised is {error}")

get_hostname_IP()

#Output:
"""
    Please enter a website addresss(URL) : www.google.com
    Hostname : www.google.com
    IP : 142.250.67.196
"""