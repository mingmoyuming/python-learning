import threading, multiprocessing

def loop():
    x = 2
    while True:
        x = x ^ 2

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
