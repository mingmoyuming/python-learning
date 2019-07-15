import asyncio

def calback(seleep_time,loop):
    print("seleep_time {} success".format(seleep_time))

def stop_loop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    loop.call_at(now+2, calback, 2)
    loop.call_at(now+1, calback, 1)
    loop.call_at(now+3, calback, 3)
    #loop.call_soon(stop_loop,loop)
    loop.call_soon(calback,4)
    loop.run_forever()