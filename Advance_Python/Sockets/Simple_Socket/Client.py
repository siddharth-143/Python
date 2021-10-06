# Client

import socket

# socket object to establish the connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to web server on port 80
client_socket.connect(("www.google.com", 80))