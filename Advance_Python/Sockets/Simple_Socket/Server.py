# server

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host
server_socket.bind((socket.gethostname(), 80))


# server socket and listen for connections
server_socket.listen(5)