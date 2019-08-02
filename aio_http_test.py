#全自动自助添加航班号查询价格

import aiohttp
import asyncio

import re
import aiomysql
import json


watting_aircraft = []
seen_url = set()
heads = {
    'accept': '*/*',
    'content-type': 'application/json',
   # 'content-length:': '63',
   # ':path': '/itinerary/api/12808/lowestPrice',
   # ':authority': 'flights.ctrip.com',
    'origin': 'https://flights.ctrip.com',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/xmn-ten?date=2019-08-02',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'accept-encoding': 'gzip, deflate, br',
    'cookie': '_RSG=okKgVzoX7wEodJoglQS5.A; _RDG=2881c732faab6c21973ff9911cf32ef7d5; _RGUID=ee87872f-5fa9-4bb2-af85-71abeac939f2; _ga=GA1.2.1422720350.1563249755; _abtest_userid=be1c9d71-993c-4798-8f79-14b86a08cce3; gad_city=68ab5ca41443a3ca10068e9f21606707; _gid=GA1.2.426601872.1564220734; MKT_Pagesource=PC; DomesticUserHostCity=XMN|%cf%c3%c3%c5; _RF1=36.249.172.214; appFloatCnt=6; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1564849588894; FD_SearchHistorty={"type":"S","data":"S%24%u53A6%u95E8%28XMN%29%24XMN%242019-08-02%24%u94DC%u4EC1%28%u94DC%u4EC1%u51E4%u51F0%u673A%u573A%29%28TEN%29%24TEN%24%24%24"}; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D36%26v2%3D32; _bfa=1.1563249751667.2lgf0g.1.1564224091868.1564241727769.4.42; _bfs=1.33; _gat=1; _jzqco=%7C%7C%7C%7C%7C1.491324463.1563249754461.1564246125860.1564246193816.1564246125860.1564246193816.0.0.0.35.35; __zpspc=9.6.1564244788.1564246193.26%232%7Cwww.baidu.com%7C%7C%7C%7C%23'}
         #'accept-language': 63,
         #'Cookie': cookie}
    #}
request_payload = {
    'flightWay': "Oneway",
    'dcity': "xmn",
    'acity': "ten",
    'army': 'false'
}

async def get_url(session,url):
    async with session.post(url, data=json.dumps(request_payload), headers=heads) as respones:
        return await respones.json()

async def main():
    url = "https://flights.ctrip.com/itinerary/api/12808/lowestPrice"
    async with aiohttp.ClientSession() as session:
        html = await get_url(session, url)
        print(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
