import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

# def handle_sock(sock,addr):
def handle_sock(sock, addr):
    while True:
        re_data = input()
        sock.send(re_data.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))

#获取客户端发送的数据
while True:
    sock, addr = server.accept()
    #用线程去处理新接受的连接
    client_thred = threading.Thread(target=handle_sock, args=(sock,addr))
    client_thred.start()

    # data = sock.recv(1024)
    # # sock.send("hello boby".encode('utf-8'))
    # print("客户端发送"+data.decode('utf-8'))
    # re_data = input("你")
    #
    # sock.send(re_data.encode('utf-8'))
    # server.close()
    # sock.close()