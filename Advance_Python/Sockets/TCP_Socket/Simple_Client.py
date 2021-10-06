# simple client

import socket

s = socket.socket()

# get the current machine name
host = socket.gethostname()

# define the port on which you are connect
port = 12345

# connect ti the server on local computer
s.connect((host, port))

# receive data from the server and decoding to get the string
print(s.recv(1024).decode())

# close the connection
s.close()