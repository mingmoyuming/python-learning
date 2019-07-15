import requests
from urllib import parse
import time
import urllib.request
import strip
import re



# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

# def a(i):
#     a = 1
#     b = 2
#     c = 3
# #     d = i
# #     return a, b, c, d
# #
# # if __name__ == '__main__':
# #     e,f,g,h = a(2)
# #     print(e,f,g,h)
#
#
# with open('a.txt', 'r',encoding='utf-8') as f:
#     b = f.read()
#     a = eval(b)


# from urllib import parse
#
# data = {'a': '黄鹤', 'name': '小姨子', '特权': '没有'}
#
# print(parse.urlencode(data))

# from urllib import parse
#
# data = '双叶爱heh你爹来了'
# print(parse.quote(data))
#
# import time
# a = (time.strftime("%Y %m %d "))
# print(type(a))

# import urllib.request
# from urllib import parse
# import strip
# import re
# a = ('https://news.163.com/19/0624/08/EIE225JJ0001899O.html', "<em class='fB cms-I_Blank_'>央视:操场埋尸案令人毛骨悚然 邓之死谜团尚未揭开</em>")
# b = re.findall('<em.*?>(.*?)</em>', a[1])
# #print(type(a))
# for i in b:
#     print(i)
# print(b)
# # c = (a[0], b)
# print(type(b))
# # print()

#支持markdown
# wz = "每日新闻"
# nr = """
# 今天是2019年06月24日，今天的新闻有：
# ('https://news.163.com/19/0624/15/EIEPR501000189FH.html', '习近平访朝是一次友好之旅、和平之旅')
# ('https://news.163.com/19/0624/12/EIEEQ69S000189FH.html', '外交部就习近平出席G20峰会举行中外媒体吹风会')
# ('https://news.163.com/19/0624/15/EIEQFTLC000189FH.html', '中国饭碗：让近14亿人吃饱吃好 为世界贡献方案')
# ('https://news.163.com/19/0624/15/EIEQJKG1000189FH.html', '中国自贸试验区推动多领域与国际先进制度对标')
# ('https://news.163.com/19/0624/15/EIEQT9LP000189FH.html', '创新方式方法 学懂弄通做实  ')
# ('https://news.163.com/19/0624/08/EIE225JJ0001899O.html', "<em class='fB cms-I_Blank_'>央视:操场埋尸案令人毛骨悚然 邓之死谜团尚未揭开</em>")
# ('https://news.163.com/19/0624/15/EIER4BBU000189FH.html', '“第一书记”黄文秀：初心不灭 青春无悔 ')
# ('https://news.163.com/19/0624/11/EIECQFBV000189FH.html', '中国正处在迈向现代化关键期')
# ('https://news.163.com/19/0624/09/EIE6CRHI000189FH.html', '人民日报:单边主义没有未来')
# ('https://news.163.com/19/0624/15/EIES108M000189FH.html', '北京市禁毒办推出禁毒公益歌曲《绝不宽恕》')
# ('https://news.163.com/19/0624/13/EIEIOIEH0001899O.html', '广东茂名市政协主席溺水身亡 警方正作进一步调查')
# ('https://news.163.com/19/0624/10/EIE901P80001899N.html', '台媒:美侦察机接近至台湾岛12海里处 后飞往南海')
# ('https://news.163.com/19/0624/08/EIE2SNTQ0001899N.html', '特朗普:博尔顿绝对是鹰派 若由他决定他会挑战世界')
# ('https://news.163.com/19/0624/14/EIEMSH740001899O.html', '韩总统府:特朗普29日访韩 30日同文在寅举行会晤')
# ('https://news.163.com/19/0624/07/EIDUOH4E0001899O.html', '宜宾震区成群飞的是啥?官方:有3种可能 与地震无关')
# ('https://news.163.com/19/0624/14/EIEMBPO50001899N.html', '广西帅气学霸高考730分：英语数学双满分！')
# ('https://news.163.com/18/1229/13/E46QMLQH000189FH.html', '前11个月国企利润同比增长15.6% ')
# ('https://news.163.com/19/0624/11/EIEDR4S800018AOR.html', '湖北高考理科第1名4年前曾上北大 因打游戏被劝退')
# ('https://news.163.com/19/0624/07/EIE0I7FO0001899N.html', '宜兴紫砂壶黑幕:百元"枪手壶"刻大师名章卖几十万')
# ('https://news.163.com/19/0624/13/EIEKQ16T0001899N.html', '广西最高分考生全家北清复交？考了730分的他辟谣')
# ('https://news.163.com/19/0624/09/EIE6DA0L0001899O.html', '笑死人了?男子开玩笑把邻居笑死 赔6万还险被判刑')
# ('https://news.163.com/19/0624/15/EIEQLF6K0001875P.html', '"埋尸案"受害者家属律师:家属情绪崩溃 盼查明真相')
# ('https://news.163.com/19/0624/14/EIEMQCAT0001899N.html', '广东茂名市政协主席溺亡 官方:尚不能确定死亡原因')
# ('https://news.163.com/19/0621/19/EI7HVK4S0001899O.html', '周永康、孙政才案审判长 再审这个重要案件')
# """
# print(nr)
# # wz = parse.quote(wz)
# # nr = parse.quote(nr)
# # print(wz)
# print(nr)
# #https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send?text=%E4%B8%BB%E4%BA%BA%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8F%88%E6%8C%82%E6%8E%89%E5%95%A6~&desp=%E5%95%8A%E5%95%8A%E5%95%8A%E5%95%8A
# heads = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
# diz = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send?text="+wz+"&desp="+nr
# f = urllib.request.Request(diz)
# z = urllib.request.urlopen(f).read()
# # print(z)
#
# import time
#
# bt = "今天是%s，今天的新闻有：" % time.strftime("%Y{}%m{}%d{}").format('年', '月', '日')
# print(bt)

#api = "https://sc.ftqq.com/SCU5553Tb223e134f4ad5f783c91938a8f9e4b40588ee5a731041.send"
# api = "https://sc.ftqq.com/SCU5ssssss553Tb223e134f4adsssssssssss5f783c9SSSSSSS1938a8f9e4b40588ee5a731041.send"
# title = u'通知1'
# connect = """
# #服务器炸了
# ##赶紧抢修啊
# ###你在干嘛1
# """
# data = {'text': title, 'desp': connect}
#
# import requests
# req = requests.post(api, data=data)
# print(req)

import strip
# a="httpa://aabcacb1111acbba.com"
# print(a.strip("abc"))
# print(api.strip("s"))



ym = """
/***
 *                                         ,s555SB@@&
 *                                      :9H####@@@@@Xi
 *                                     1@@@@@@@@@@@@@@8
 *                                   ,8@@@@@@@@@B@@@@@@8
 *                                  :B@@@@X3hi8Bs;B@@@@@Ah,
 *             ,8i                  r@@@B:     1S ,M@@@@@@#8;
 *            1AB35.i:               X@@8 .   SGhr ,A@@@@@@@@S
 *            1@h31MX8                18Hhh3i .i3r ,A@@@@@@@@@5
 *            ;@&i,58r5                 rGSS:     :B@@@@@@@@@@A
 *             1#i  . 9i                 hX.  .: .5@@@@@@@@@@@1
 *              sG1,  ,G53s.              9#Xi;hS5 3B@@@@@@@B1
 *               .h8h.,A@@@MXSs,           #@H1:    3ssSSX@1
 *               s ,@@@@@@@@@@@@Xhi,       r#@@X1s9M8    .GA981
 *               ,. rS8H#@@@@@@@@@@#HG51;.  .h31i;9@r    .8@@@@BS;i;
 *                .19AXXXAB@@@@@@@@@@@@@@#MHXG893hrX#XGGXM@@@@@@@@@@MS
 *                s@@MM@@@hsX#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,
 *              :GB@#3G@@Brs ,1GM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B,
 *            .hM@@@#@@#MX 51  r;iSGAM@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@8
 *          :3B@@@@@@@@@@@&9@h :Gs   .;sSXH@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
 *      s&HA#@@@@@@@@@@@@@@M89A;.8S.       ,r3@@@@@@@@@@@@@@@@@@@@@@@@@@@r
 *   ,13B@@@@@@@@@@@@@@@@@@@5 5B3 ;.         ;@@@@@@@@@@@@@@@@@@@@@@@@@@@i
 *  5#@@#&@@@@@@@@@@@@@@@@@@9  .39:          ;@@@@@@@@@@@@@@@@@@@@@@@@@@@;
 *  9@@@X:MM@@@@@@@@@@@@@@@#;    ;31.         H@@@@@@@@@@@@@@@@@@@@@@@@@@:
 *   SH#@B9.rM@@@@@@@@@@@@@B       :.         3@@@@@@@@@@@@@@@@@@@@@@@@@@5
 *     ,:.   9@@@@@@@@@@@#HB5                 .M@@@@@@@@@@@@@@@@@@@@@@@@@B
 *           ,ssirhSM@&1;i19911i,.             s@@@@@@@@@@@@@@@@@@@@@@@@@@S
 *              ,,,rHAri1h1rh&@#353Sh:          8@@@@@@@@@@@@@@@@@@@@@@@@@#:
 *            .A3hH@#5S553&@@#h   i:i9S          #@@@@@@@@@@@@@@@@@@@@@@@@@A.
 *
 *
 *    又看源码，看你妹妹呀！
 */
"""

# # print(ym)
#
#
# a = {'errno': 0, 'errmsg': 'success', 'dataset': 'done'}
# if a['errno'] == 0:
#     print("发送成功！")

# import re
# a = "sssasdafdsaffsabcjasncjnjvsssssssssncjvncdmvkdfmbvkmckxmbxcvbcxbasdawdqdssvscvdxbxwdda"
# # f = re.sub(a,"s")
# f = a.strip("s,s").strip("s")
# print(f)
# import os
# a = r"http://comment.tie.163.com/EIIBH5S50001875P.html"
# f = os.path.basename(a)
# print(f)
#
# a = "-"
# b = ("a", "b", "c")
# df = a.join(b)
# print(type(b))


# url = "http://httpbin.org/cookies"
#
# a = {'name': 'Tian', 'sex': '1'}
# f = requests.get(url, cookies=a)
# print(f.json())


#github模拟登陆
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'github.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

s = requests.session()
s.headers.update(headers)



#
def get_token():
    url = "https://github.com/login"
    respet = s.get(url, timeout=10)
    pat = 'name=\"authenticity_token\" value=\"(.*?)\"'
#    print(respet.json())
    print(re.findall(pat, respet.text)[0])
    resut = re.findall(pat, respet.text[0])
    #print(resut)
    return resut


# def login(authenticity_token,account,passwd):
#     url = "https://github.com/session"
#     data1 = {'commit': 'Sign in',
#             'utf-8': '\u2713',
#             'authenticity_token': authenticity_token,
#             'login': account,
#             'password': passwd,
#             }
#     f = requests.post(url, data=data1)
#     print(f.text)




if __name__ == "__main__":
    account, passwd = '1076776375@outlook.com', 'pGe4Ci8P'
    authenticity_token = get_token()
    #print(authenticity_token)
    # login(authenticity_token, account, passwd)


# print(ym)