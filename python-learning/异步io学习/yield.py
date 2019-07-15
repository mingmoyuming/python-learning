import asyncio
import time

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


# def a():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print("这是循环第%s" % n)
#         r = '200'
#
# def b(c):
#     c.send(None)
#     n = 0
#     while True < 5:
#         print("输出 %s" %n)
#         r = c.send(n)
#         print("输出200 是：%s" % r)
#     c.close()
#
# c = a()
# b(c)



# def a():
#     r = ''
#     while True:
#         s = yield r
#         if not s:
#             pass
#         print("接收到的值为b传送过来的值，需要注意，这是协程。不是同步.传送过来的值为：%s" %s)
#         r = "200 OK "#此值传送到b也就是说a和b建立了通道，无需经过同步
#
# def b(c):  #此函数是发送作用，也就 是传r值
#     n = 0 #初始值
#     c.send(None)  #第一次必须发送任意的值或是None进行激活
#     while n < 500000:
#         n += 1
#         print("此时n的值应该与a函数一样，发送值为 %s" %n)
#         r = c.send(n)
#         #此时r函数应该通用
#         print("%s" %r)
#     c.close()
#
#
# if __name__ == "__main__":
#     start = time.time()
#     c = a()
#     b(c)
#     print("异步io耗时 %.2f" % (time.time() - start))


# def a():
#     r = ''
#     while True:
#         s = yield r
#         if not s:
#             pass
#         print("第%s次" %s)
#         r = "200 ok"
#
#
#
# def b(c):
#     n = 0
#     c.send(None)
#     while n < 5:
#         n += 1
#         r = c.send(n)
#         print("值 %s" %r)
#
#
#
# if __name__ == "__main__":
#     c = a()
#     b(c)

#普通协程


# def a():
#     start = time.time()
#     print("开始读取..")
#     time.sleep(2)
#     print("读取完成，耗时 %2.f" %(time.time() - start))
#
#
# def b():
#     start = time.time()
#     print("开始读取2号文件...")
#     time.sleep(3)
#     print("读取2号文件完成，耗时 %2.f" % (time.time() - start))
#
#
# if __name__ == "__main__":
#     start = time.time()
#     a()
#     b()
#     print("总耗时%f" %(time.time() - start))


# def a(title):
#     yield title
#
# def b(title):
#     yield from title
#
# title = ['Python','JAVA','C++']
#
# for tit in a(title):
#     print('生成器', tit)
#
# for tit in b(title):
#     print('生成器2', tit)

# async def a():
#     print("任务1开始io")
#     await asyncio.sleep(5)
#     print("任务执行完成耗时3秒")
#     return a.__name__
#
# async def b():
#     print("任务2开始io")
#     await asyncio.sleep(3)
#     print("任务2执行完成耗死5秒")
#     return b.__name__
#
# async def main():
#     task = [a(),b()]
#     wc, sb = await asyncio.wait(task)
#     for i in wc:
#         print('协程无序返回值：', i.result())
#
# if __name__ == "__main__":
#     start =time.time()
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(main())
#     finally:
#         loop.close()
#     print("耗时%.5f" %(time.time() - start))


# from itertools import chain
#
#
# my_list = [1,2,3]
# my_dict = {"boby1":"http://www.baidu.com",
#            "boby2":"http://www.immcoo.com",}
# for value in chain(my_dict, my_list, range(5, 10)):
#     print(value)
#
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         for


my_data = {"面膜" : [1, 2, 3, 4]}

for i,f in my_data.items():
    print(i)
    print(f)
