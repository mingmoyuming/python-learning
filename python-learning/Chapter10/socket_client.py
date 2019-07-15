

import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
client.send("hello".encode('utf-8'))
while True:
    # data = client.recv(1024)
    # print(data.decode('utf-8'))
    re_data = input("你：")
    client.send(re_data.encode('utf-8'))
    data = client.recv(1024)
    print("服务器端发送:"+data.decode('utf-8'))
    # client.close()