
import urllib.request
import request
import urllib3
import sys

heasd = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#关闭ssl验证

#sys.setdefaultencoding('utf8')
f = open('html.txt', 'w', encoding='utf-8')
http = urllib3.PoolManager()
data = http.request('GET', "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8F%8C%E5%8F%B6%E6%9D%8F")
print(data.data.decode())
f.write(data.data.decode())
f.close()
# http = urllib3.PoolManager()
# data = http.request('GET', "https://tieba.baidu.com/f?fr=wwwt&kw=008")
# if data.status == 200:
#     print("返回值200，正常")
# print(data.data.decode())
#

# #等同于
# html = urllib.request.Request("https://tieba.baidu.com/f?fr=wwwt&kw=008")
# html_connect = urllib.request.urlopen(html).read()
# html_connect = html_connect.decode('utf-8')
# print(html_connect)