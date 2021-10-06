# UDP Socket Client

import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 12345

msg = "welcome to socket programing"
print("UDP target IP : ", host)
print("UDP target Port : ", port)

# sending the message to UDP server
udp_socket.sendto(msg.encode(), (host, port))