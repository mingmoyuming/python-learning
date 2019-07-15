import aiohttp
import asyncio
import re
import time

urls = [
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16488',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16380',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16911',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16581',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16674',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16112',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/17343',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16659',
    'https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16449',
]
title = []
sem = asyncio.Semaphore(10)

async def fetch(url):
    with(await sem):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                r = re.compile('id="title"(.*?)</div>')
                f = re.findall(r, html)
                print(f)

def main():
    loop = asyncio.get_event_loop()
    task = [fetch(url) for url in urls]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()


if __name__ == "__main__":
    start = time.time()
    main()
    print("耗时%s" %(time.time() - start))