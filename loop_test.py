
# import asyncio
# import time
# from functools import partial
# async def get_url(url):
#     print("开始 %s" %url)
#     await asyncio.sleep(2)
#     #time.sleep(2)
#     return url
#
# def callback(a,b):
#     print(a)
#     print("send email to bobbt")
#
#
# if __name__ == '__main__':
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     #get_future = asyncio.ensure_future(get_url("http://www.baidu.com")) #获取返回值二选一都可以
#     task = loop.create_task(get_url("www.google.com"))
#     #task.add_done_callback(partial(callback, "www.hexie.com"))
#     loop.run_until_complete(task)
#     print(task.result())
#     print("耗时",time.time() - start,"秒")


#task 和gather区别


import asyncio
import time
# from functools import partial
# async def get_url(url):
#     print("开始 %s" %url)
#     await asyncio.sleep(2)
#     #time.sleep(2)
#     return url
#
# # def callback(a,b):
# #     print(a)
# #     print("send email to bobbt")
#
#
# if __name__ == '__main__':
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     #get_future = asyncio.ensure_future(get_url("http://www.baidu.com")) #获取返回值二选一都可以
#     task = [get_url("www.google.com") for i in range(10)]
#     #task.add_done_callback(partial(callback, "www.hexie.com"))
#     loop.run_until_complete(asyncio.gather(*task))
# #    print(task.result())
#     print("耗时",time.time() - start,"秒")
#
# #gather 和wait区别
# #gather更加hight-level
#     task1 = [get_url("www.abczg.tro") for i in range(2)]
#     task2 =

# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()

#
#以下为停止协程
async def html_urt(url):
    print("start")
    await asyncio.sleep(url)
    print("done aftert {}s".format(url))

#
#
# if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task1 = html_urt(2)
    task2 = html_urt(3)
    task3 = html_urt(3)
#
    tasks = [task1, task2, task3]
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e :
#         all_task = asyncio.all_tasks()
#         for task in all_task:
#             print("cancel task")
#             print(task.cancel())
#         loop.stop()
#         loop.run_forever()
#     finally:
#         loop.close()

        # try:
        #     loop.run_until_complete(asyncio.wait(tasks))
        # except KeyboardInterrupt as e:
        #     all_task = asyncio.all_tasks()
        #     for i in all_task:
        #         print("结束协程")
        #         i.cancel()
        #     loop.stop()
        #     loop.run_forever()
        # finally:
        #     loop.close()
        # try:
        #     loop.run_until_complete(asyncio.wait(tasks))
        # except KeyboardInterrupt as e:
        #     all_task = asyncio.all_tasks()
        #     for i in all_task:
        #         print("协程已经结束")
        #         i.cancel()
        #     loop.stop()
        #     loop.run_forever()
        # finally:
        #     loop.close
    try:
        loop.run_until_complete(tasks)
    except KeyboardInterrupt as e:
        all_task = asyncio.all_tasks()
        for i in all_task:
            print("协程结束")
            i.cancel()
        loop.stop()
        loop.run_until_complete()
    finally:
        loop.close()