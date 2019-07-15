import threading
import time



# def add(n):
#     print("task", n)
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#     time.sleep(1)
#     print('0s')
#     time.sleep(1)
#
#
#
# if __name__ == "__main__":
#     f1 = threading.Thread(target=add, args=("n1",))
#     f2 = threading.Thread(target=add, args=("n2",))
#
#     f1.start()
#     f2.start()
#     f1.join()
#     f2.join()

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须要写
        self.n = n

    def run(self):
        print("task", self.n)
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('0s')
        time.sleep(1)


if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")

    t1.start()
    t2.start()