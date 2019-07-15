#网易云所有新闻爬取并存入数据库
#使用异步io
#已知有10个url，进行异步爬取
import aiohttp
import aiomysql
import asyncio
import re
import time
from lxml_text import etree

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

async def html_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            r = re.compile('<div id="title">(.*?)</div>')
            f = re.findall(r, html)
            print(f)


def main():
    loop = asyncio.get_event_loop()
    task = [html_url(url) for url in urls]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()




if __name__ == "__main__":
    start = time.time()
    main()
    print("结束耗时%s " %(time.time() - start))


