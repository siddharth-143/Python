# simple server

import socket

# create a socket
s = socket.socket()
print("Socket successfully create")

port = 12345

# bind to the port
s.bind(("", port))

# put the socket into listening mode
s.listen(5)
print("socket bind to %s" %(port))

while True:
    # establish the connection with client
    c, addr = s.accept()
    print("Got connection from", addr)

    # send a thanks message to the client encoding to send byte type
    c.send("Thanks for connecting".encode())

    # close the connection
    c.close()
    break
