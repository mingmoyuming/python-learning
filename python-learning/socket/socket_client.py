import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 199))

while True:
    send = input()
    s.send(send.encode('utf-8'))
    a = s.recv(1024)
    print(a.decode('utf-8'))
