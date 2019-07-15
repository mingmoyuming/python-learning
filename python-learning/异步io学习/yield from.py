#yield from

import time
import asyncio

async def html_url(url):
    print("开始下载", url)
    await asyncio.sleep(3)
    print("%s下载完成" %url)


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = [html_url("http://www.baidu.com"), html_url("https://www.zhihu.com")]
    loop.run_until_complete(asyncio.wait(tasks))
    print("耗时%s"%(time.time() - start ))