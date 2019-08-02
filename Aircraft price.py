# -*- coding: utf-8 -*-
#说明：此用于携程

import asyncio
import requests
import re
import time
import json
from lxml import etree
import MySQLdb
import socket

db = MySQLdb.connect("47.106.203.183", "root", "aA123.com", "Aircraft price", charset='utf8')
ins = 0
cookie = """
_RSG=okKgVzoX7wEodJoglQS5.A; _RDG=2881c732faab6c21973ff9911cf32ef7d5; _RGUID=ee87872f-5fa9-4bb2-af85-71abeac939f2; _ga=GA1.2.1422720350.1563249755; _abtest_userid=be1c9d71-993c-4798-8f79-14b86a08cce3; gad_city=68ab5ca41443a3ca10068e9f21606707; _gid=GA1.2.426601872.1564220734; MKT_Pagesource=PC; DomesticUserHostCity=XMN|%cf%c3%c3%c5; _RF1=36.249.172.214; appFloatCnt=6; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&Expires=1564849588894; FD_SearchHistorty={"type":"S","data":"S%24%u53A6%u95E8%28XMN%29%24XMN%242019-08-02%24%u94DC%u4EC1%28%u94DC%u4EC1%u51E4%u51F0%u673A%u573A%29%28TEN%29%24TEN%24%24%24"}; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D36%26v2%3D32; _bfa=1.1563249751667.2lgf0g.1.1564224091868.1564241727769.4.42; _bfs=1.33; _gat=1; _jzqco=%7C%7C%7C%7C%7C1.491324463.1563249754461.1564246125860.1564246193816.1564246125860.1564246193816.0.0.0.35.35; __zpspc=9.6.1564244788.1564246193.26%232%7Cwww.baidu.com%7C%7C%7C%7C%23
"""
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
    'dcity': "ten",
    'acity': "xmn",
    'army': 'false'
}

def price():
    url = "https://flights.ctrip.com/itinerary/api/12808/lowestPrice"
    data = requests.post(url, data=json.dumps(request_payload), headers=heads)
    data = data.json()
    # print(data['data']['oneWayPrice'])
    #f = json.dump(data)

    # nr = re.compile('\"20190802\":(.*?),')
    # sz = re.findall(nr, data)
    print(data)


def sendwechatin(price):
    price = str(price)
    bt = "主人，机票价格一直处于700以上"
    nr = "别买了，买个锤子坐大巴吧,现在的价格是:"+price
    api = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send"
    data = {'text': bt,
            'desp': nr}
    bat = requests.post(api, data=data)
    f = bat.json()
    if f['errno'] == 0:
        print("发送成功")
    elif f['errno'] == 1024:
        print("发送失败，可能是数据重复了")

def sendwechatde(price,i):
    price, i = str(price), str(i)
    bt = "厦门到铜仁价格为"+price+"第"+i+"次发送"
    api = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send"
    data = {'text': bt, 'desp': '1111'}
    bat = requests.post(api, data=data)
    f = bat.json()
    if f['errno'] == 0:
        print("发送成功")
    elif f['errno'] == 1024:
        print("发送失败，可能是数据重复了")


if __name__ == "__main__":
    frequency = 0
    #while True:
    date_price = {}
    f = price()
    print(f)
    f = f['data']['oneWayPrice']
    #print(type(f))
    for i in f:
        for k, v in i.items():
            date_price.setdefault(k, v)
    # print(date_price)
    #想要乘坐的日期
    date_want = date_price['20190802']
    #print(date_want)
    # print(f)
    # print(type(f))
    # for i in f:
    #resut = list(map(int, f))
    if date_want > 700:
        if frequency > 50:
            sendwechatin(date_want)
            frequency = 0
        frequency += 1
        #print(frequency)
    else:
        for i in range(3):
            sendwechatde(date_want, i)
            time.sleep(3)
    #以下是写入数据库
    # date_price = str(date_price)
    datatime1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    datatime1 = str(datatime1)
    cursor = db.cursor() #使用cursor()方法操作游标
    sql = "select price from 9H8398" #查询语句
    # try:
    #     cursor.execute(sql) #执行语句
    #     result = cursor.fetchall()
    #     print(result)
    # except:
    #     print("Error: unable to fecth data")
    date_price = str(date_price)
    if ins == 0:
        try:
            sql = "INSERT INTO `9H8398` (`time`, `date`, `price`) value (\""+datatime1+"\",\""+datatime1+"\",\""+date_price+"\")" #插入值
            cursor.execute(sql)
            db.commit()
            ins = 0
        except:
            print("INSERT error!")
    ins += 1
    #time.sleep(300)
    db.close()