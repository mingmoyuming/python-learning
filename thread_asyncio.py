#使用多线程：在携程中集成阻塞IO
import asyncio
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path == "/"
    #建立sock连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.setblocking(flase)
    client.connect((host),80)
    client.send("GET {} HTTP/1.1\r\nHost:")

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode("utf-8")
    html_data = data.split("\r\b\r\b")[1]
    print(html_data)
    client.close()



if __name__ =="__main__":
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    loop.run_in_executor(executor,get_url,"http://imooc.com")