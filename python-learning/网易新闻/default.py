#狗屎代码
#Shit code


#coding:utf-8
import requests
from urllib import parse
import urllib3
import urllib.request
import re
import time
import strip

heads = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}


hq = []
zw = """

"""
def news(url):
    # f = urllib.request.Request(url, headers=heads)
    # read = urllib.request.urlopen(f).read()
    # try:
    #     read = read.decode('utf-8')
    # except UnicodeDecodeError:
    #     read = read.decode('GBK')
    f = requests.get(url, headers=heads)
    read = f.text
    #r = re.compile('<li.*?><a href="(.*?)">(.*?)</a>')
    nr = re.findall('<li.*?><a href="(.*?)">(.*?)</a>', read)
    #print(nr)
    return nr

def sendwechat():
    bt = "每日新闻"
    rq = "今天是%s，今天的新闻有：" %time.strftime("%Y{}%m{}%d{}").format('年', '月', '日')
    api = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send"
   #  bt = parse.quote(bt)
   #  rq = parse.quote(rq)
   #  news_nr = parse.quote(zw)
   #  #diz = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send?text="+bt+"&desp="+rq+news_nr
   #  #f = urllib.request.Request(diz, headers=heads)
   # # read = urllib.request.urlopen(f).read()
   #  print(news_nr)
    data = {'text': bt, 'desp': rq+zw}
    bat = requests.post(api, data=data, headers=heads)
    #if '200' in bat:
    f = bat.json()
   # print(type(f['errno']))
    print(f['errno'])
    if f['errno'] == 0:
        print("发送成功")
    elif f['errno'] == 1024:
        print("发送失败，可能是数据重复了")

if __name__ == "__main__":
    global zw
    start = time.time()
    js = 0
    #print("今天是%s，今天的新闻有：" %time.strftime("%Y{}%m{}%d{}").format('年', '月', '日'))
    nr = news("https://www.163.com/")
    for i in nr:
        if 'news' in i[0] and len(i[1]) > 5:
        # if len(i[1]) > 5:
            if 'open' in i[0]:
                continue
            elif i[1] in hq:
                continue
            #print(i)
            hq.append(i[1])
            zw += '#### '+str(i)+"\n"
            js += 1
            #print(len(i[1]))
        else:
             continue
        # print(i)
        # print(len(i[1])
    print(zw)
    print("有%s条可读新闻" %js)
    #sendwechat()
    print("耗时%s秒"%(time.time() - start))
    sendwechat()
#评论http://comment.tie.163.com/EIIBH5S50001875P.html
