import aiohttp
import asyncio
import threading

# @asyncio.coroutine
# def hello():
#     print("hello,world! 线程：%s " %threading.current_thread())
#
#     yield from asyncio.sleep(1)
#
#     print("hello,again! 线程：%s" %threading.current_thread())
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     task = [hello(), hello()]
#     loop.run_until_complete(asyncio.wait(task))
#     loop.close()

# def a():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[consumer] consuming ^%s ' %n)
#         r = '200 OK'
#
# def b(c):
#     c.send(None)
#     n = 0
#     while True:
#         n += 1
#         print('[PRODUCER] producing %s' %n)
#         r = c.send(n)
#         print('[PROUCER consumer treunt %s' %r)
#     c.close()
#
# c = a()
# b(c)




import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
