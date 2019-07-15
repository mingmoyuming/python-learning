#asyncio爬虫去重，入库
import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = "https://www.freebuf.com"
waitting_urls = []
seen_urls = set()
stopping = False


async def fetch(url,session):
        try:
            async with session.get(url) as resp:
                print("url status:{}".format(resp)
                    if resp.status in [200.201]:
                        data = await resp.text()
                        return data
        except Exception as e:
            print(e)

def extracet_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls

def extract_urls(html):
    urls = []
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waitting_urls.append(url)
    return urls


async def init_urls():
    html = await fetch(start_url)
    extracet_urls(html)

async def article_handler(url,session,pool):
    #获取文章详情并解析入库
    html = await fetch(url, session)
    seen_urls.add(url)
    extracet_urls(html)
    pq = PyQuery(html)
    title = pq('title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert in to spider(name) value({})".format(title)
            await conn.execute(insert_sql)




async def consumer(pool):
    async with aiohttp.ClientSession() as session:
        while not stopping:
            if len(waitting_urls) == 0:
                await asyncio.sleep(0.5)
                continue

            url = waitting_urls.pop()
            print("start get url:{}".format(url))
            if re.match('http://.*?freebuf.com/.*?/.*?/\d+.html', url):
                if url not in seen_urls:
                    asyncio.ensure_future(article_handler(url,session, pool))
            else:




async def main(loop):
    #等待mysql连接建立
    pool = await aiomysql.create_pool(host='47.106.203.183', port='3306', user='root', password='aA123.com',db = 'bysj',loop=loop,charset = 'urf-8', autocommit=True)
    asyncio.ensure_future(init_urls())
    asyncio.ensure_future(consumer(pool))
