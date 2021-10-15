import socket

s = socket.socket()

host = socket.gethostname()

port = 12345

s.connect((host, port))

msg = input("->")

while msg.lower().strip() != 'bye':
    s.send((msg.encode()))
    data = s.recv(2014).decode()
    print("Received form server : ", data)
    msg = input("->")

s.close()