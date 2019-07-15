import socket
from urllib.parse import urlparse
from lxml import etree

def http_main(url):
    url2 = urlparse(url)
    host = url2.netloc
    path = url2.path
    if path == "":
        path = "/"


    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8'))
    # client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8'))

    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    data_html = data.split('\r\n\r\n')[1]
    print(data_html)
    client.close()
    #print(url2)
    return etree.HTML(data_html)


if __name__ == "__main__":
    url = "https://www.baidu.com"
    f = http_main(url)
    #print(f.xpath('//@href'))
    #print(f.xpath('//text()'))
