import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #socketAF_INET为ipv4 ipv6为AF＿INET6   SOCK_STREAM为tcp连接
s.bind(("0.0.0.0", 199))
s.listen()
sock, addr = s.accept()

start = time.time()
while True:
    a = sock.recv(1024)
    if a.decode('utf-8') == 'bye':
        sock.send("bye 7535".encode('utf-8'))
        s.close()
        break
    print(a.decode('utf-8'))
    send = input()
    sock.send(send.encode('utf-8'))
print("运行已结束，正常运行了{}秒".format((time.time() - start)))
#
# #多线程
# def socket():
#     sock, addr = s.accept()
#     while True:
#         sock.send("你好，客户端，我是服务端，为您服务".encode('utf-8'))
#         js  = sock.recv(1024).decode('utf-8')
#         print(js)
#         if js ==  'bye':
#             sock.close()
#             break
#         else:
#             fs = input("你输入你要发送的值")
#             sock.send(fs.encode('utf-8'))
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=socket)
#     #t2 = threading.Thread(target=socket)
#     t1.start()
#     #t2.start()
#     t1.join()
#     #t2.join()