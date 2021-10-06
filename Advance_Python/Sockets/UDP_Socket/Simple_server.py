# UDP Socket server

import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 12345

# bind
udp_socket.bind((host, port))

while True:
    print("Waiting for client...")
    conn, addr = udp_socket.recvfrom(1024)
    print("Received Message", conn, "from", addr)

udp_socket.close()