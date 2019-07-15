#搜索地址为：http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=   %E6%B8%B8%E6%88%8F
#爬虫筛选关键词为：objURL
#正确："objURL":"http://s9.knowsky.com/bizhi/l/20090808/200909181%20%2810%29.jpg"
#错误：ObjUrl":"http:\/\/img3.imgtn.bdimg.com\/it\/u=2287813293,3197706607&fm=214&gp=0.jpg","FromURL":"http:\/\/www.enterdesk.com\/download\/9139-80507\/"
import urllib.request
import re
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = ['https://ws2.sinaimg.cn/large/005PGsrdgy1g1vje0j9x1j30cp0ebjrq.jpg',
'https://ws2.sinaimg.cn/large/005PGsrdgy1g1vjg2w1x5j30u10d9wfr.jpg',
'https://ws4.sinaimg.cn/large/005PGsrdgy1g1vjx9ythvj30lc0fit9s.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vjxqeu0vj308g09mglt.jpg',
'https://ws2.sinaimg.cn/large/005PGsrdgy1g1vkl5fob8j30bp028t8p.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vklhamqzj30o10d9750.jpg',
'https://ws2.sinaimg.cn/large/005PGsrdgy1g1vklsgm4xj30lt0m6dh7.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkm55aeaj30g207nq2t.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkmfd9zdj30jj0b3jr9.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkmp64nqj30g60gadfz.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkn2kc83j30gl0f53yk.jpg',
'https://ws2.sinaimg.cn/large/005PGsrdgy1g1vkng4z1bj30e50ghaa9.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkoq4ncqj30kh06mmzv.jpg',
'https://ws2.sinaimg.cn/large/005PGsrdgy1g1vkpayfexj30c305iglm.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkplmmgcj30cp0hp74i.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkpwc67bj30g708vaa6.jpg',
'https://ws1.sinaimg.cn/large/005PGsrdgy1g1vkq8fkyij309c052gli.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkqj7dzsj30bh098a9z.jpg',
'https://ws3.sinaimg.cn/large/005PGsrdgy1g1vkqvffrtj30b5056mx0.jpg',
'https://ws1.sinaimg.cn/large/005PGsrdgy1g1vkr7m385j30av04ja9y.jpg',]

header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
sear = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8F%8C%E5%8F%B6%E6%9D%8F"

def down(url):
    path = r"E:\a small program every day\tuchuang"
    try:
        os.chdir(path)
    except FileNotFoundError as e:
        os.mkdir(path)
        os.chdir(path)
    f = os.path.basename(url)
    #r = re.findall('(...\.)', url)
    #print(r)
    try:
        urllib.request.urlretrieve(url, f)
    except TimeoutError:
        down(url)

def html_url(name):
    url = urllib.request.Request((sear+name), headers=header)
    html_connect = urllib.request.urlopen(url).read()
    try:
        html_connect = html_connect.decode('GBK')
    except UnicodeDecodeError :
        html_connect = html_connect.decode('utf-8')
    r = re.compile('objURL":"(http://.*?)"')
    result = re.findall(r, html_connect)
    return result



if __name__ == "__main__":
    file = open('lianjie.txt', 'w+', encoding='utf-8')
    #url = sear+"双叶杏"
    #print(url)
    #html = "http://b-ssl.duitang.com/uploads/item/201507/27/20150727185549_WisPY.jpeg"
    #down(html)
   # html = html_url(sear)
    for i in url:
    #    down(i)
    #     print(i)
    #     break
        down(i)
        file.write(i + '\n')#+ '\n'
    file.close()


# 你妈的，为什么？
