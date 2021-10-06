# Non Blocking Client

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

# set non blocking mode
s.setblocking(0)

data = "Hello Python \n"* 10 * 1024 * 1024

assert s.send(data.encode())