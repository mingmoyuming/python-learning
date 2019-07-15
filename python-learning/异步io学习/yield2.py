import asyncio
import time
#import asyncio


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
#             print("返回return ")
#             return
#         print("这是循环第%s" % n)
#         r = '200'
#
# def b(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print("输出 %s" %n)
#         r = c.send(n)
#         print("输出200 是：%s" % r)
#     c.close()
#
# c = a()
# b(c)
#



# yield  和 yield from 区别

# def a1(a):
#     yield a
#
# def a2(a):
#     yield from a     #for title in titles:　# 等价于yield from titles
#                                                        yield title　　
#
#
#
# a = ['JAVA', 'PYTHON', 'C++']
#
# for i in a1(a):
#     print("a1的值是",i)
#
# for i in a2(a):
#     print("a2的值是",i)
# #

#深入了解yield 和yield from

# def generator_1():
#     n = 0
#     while True:
#         r = yield
#         if not r:
#             break
#         print("加的数值为：",r)
#         n += r
#     return n
#
# def generator_2():#委托生成器
#     while True:
#         total = yield from generator_1() #子生成器
#         print("加的总和为：", total)
#
#
# if __name__ == "__main__":   #调用方
#     # g1 = generator_1()
#     # g1.send(None)
#     # g1.send(2)
#     # g1.send(3)
#     # g1.send(None)
#     g2 = generator_2()
#     g2.send(None)
#     g2.send(2)
#     g2.send(3)
#     g2.send(None)

#结合@asyncio.coroutine

#只要是有和IO任务类似的、耗费时间的任务都需要yield from 进行阻断，以达到异步的功能

#@asyncio.coroutine 表示协程装饰器


# @asyncio.coroutine
# def taskio_1():
#     print("开始任务1")
#     yield from asyncio.sleep(2)
#     print("任务1执行完成 耗时2秒")
#     return taskio_1.__name__
#
# @asyncio.coroutine
# def taskio_2():
#     print("任务2开始执行")
#     yield from asyncio.sleep(3)
#     print("任务2执行完成 耗时3秒")
#     return taskio_2.__name__
#
# #@asyncio.coroutine
# #def main():
# #    task = [taskio_1(), taskio_2()]
# #    done, peding = yield from asyncio.wait(task)
# #    for i in done:
# #        print("协程无序返回值：", i.result())
#
# if __name__ == "__main__":
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     task = [taskio_1(), taskio_2()]
#     loop.run_until_complete(asyncio.wait(task))
#     print('所有IO任务总耗时%.5f秒' % float(time.time()-start))
# #    try:
# #        loop.run_until_complete(main())
# #    finally:
# #        loop.close()
# #    print('所有IO任务总耗时%.5f秒' % float(time.time()-start))



async def a():
    print("输出开始io")
    await asyncio.sleep(15)
    print("输出完成，完成耗时15秒")

async def b():
    print("输出B")
    await asyncio.sleep(4)
    print("完成耗时4秒")



if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    task = [a(), b()]
    loop.run_until_complete(asyncio.wait(task))
    print("总耗时%s" %(time.time() - start))