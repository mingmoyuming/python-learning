# urls = [
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
#     'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
# ]
#
# for i in urls:
#     print('#'+i+'\n')

#学习self


#
# class test(object):
#     def add(self, a, b):
#         print(a+b)
#     def display(self):
#         print("hello amnghy")
#
#
# t = test
# #t.add(2,3)
# t.display()


#我写尼玛的程序fuck canpin



# class test(object):
#     def run(self, a):
#         print(self.a)
#
#     def add(self,a,b):
#         print(a+b)
#
#
# test = test
# test.run(1)

# import socket
#
# import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(12,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


# import asyncio
# import time
# #1 + 100
# f = 0
#
# async def add(rang):
#     global f
#     f += rang
#     print(f)
#     await asyncio.sleep(1)
#     return f
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     task = [add(i) for i in range(101)]
#     loop.run_until_complete(asyncio.wait(task))
#     loop.close()


#多线程执行你好(1--100)
#
# import threading
# import time
# import random
#
#
# #t1 = threading.Thread(target=run_thread, args=(5,))
#
#
# def abc(rang):
#     print(rang)
#     time.sleep(1)
#
# def run():
#     for i in range(10):
#         abc(i)
#
# if __name__ == "__main__":
#     start = time.time()
#     t1 = threading.Thread(target=run)
#     t2 = threading.Thread(target=run)
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()
#     print("耗时%s"%(time.time() - start))
# # import random
# #
# # print(random.random())


a = input("你好")
print(a)