# Blocking Client

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

# set blocking mode
s.setblocking(1)

data = "Hello Python \n"*10*1024*1024

# send data till true
assert s.send(data.encode())