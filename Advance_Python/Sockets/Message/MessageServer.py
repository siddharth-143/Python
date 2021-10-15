# Python program to implement communication between server and client

import socket

s = socket.socket()
print("Socket create successfully!")

# host number
host = socket.gethostname()

# port number
port = 12345

# bind th4 host and port so that we can communicate
s.bind((host, port))

# number of connection
s.listen(3)
print("socket bind to %s" %(port))

conn, addr = s.accept()

print("Connection from : ", str(addr))

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("From connected user : ", str(data))
    data = input("->")
    conn.send(data.encode())

conn.close()