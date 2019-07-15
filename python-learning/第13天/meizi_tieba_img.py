import os
import re
import urllib.request
import urllib3
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

cookies = 'BIDUPSID=3D39D7EE3751F21085792F9E16E889BA; PSTM=1502853788; TIEBA_USERTYPE=b202ce2234bc48a126f7e6ea; bdshare_firstime=1502853816642; FP_UID=80f976b99d32361ea8aaeaf335970118; FP_LASTTIME=1510460893642; rpln_guide=1; __cfduid=d71f07e165ce6da3f34237bdc7f7eecff1538732259; BAIDUID=75A49387A8B2787F648B39BDC61C26FF:FG=1; TIEBAUID=bcf772fd14267a23d10abf51; BDUSS=JhMWVxaEtnZ0RkOXRKaE9ZWkgzTmFqTFBWSWNCYjBoYTQ4OExSQ1I1dzJrdE5jSVFBQUFBJCQAAAAAAAAAAAEAAAD5Oy9jx-C1wLS0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYFrFw2BaxcNk; MCITY=-141%3A194%3A; STOKEN=fe3eff61f020b674f2f386c43ef414d1c699b8ac52f4a5d7db9656a601f49893; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=6; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1559472046,1559472108,1559567371,1559567815; H_PS_PSSID=1450_21078_29135_20697_28519_29099_29134_28836_28584_26350_29071; 1664039929_FRSVideoUploadTip=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1559569210'
heads = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",'Connection':"keep-alive",'Content-Type':"text/html; charset=UTF-8",
         'Cookie' : cookies}
tieba = "https://tieba.baidu.com"
img = "http://imgsrc.baidu.com/forum/pic/item/"
# url = "https://passport.baidu.com/center"
# f = urllib.request.Request(url, headers=heads)
# nr = urllib.request.urlopen(f).read()
# nr = nr.decode('utf-8')
# print(nr)
def img_down(url, uname ,len):
    f = os.path.basename(url)
    url2 = img + f
    path = r"E:\python-learning\python-learning\第13天\%s" %uname
    try:
        os.chdir(path)
    except FileNotFoundError as e:
        os.mkdir(path)
        os.chdir(path)
    path_img = os.listdir()
    # for b in range(len):
    #     if i in path_img:
    #         continue
    urllib.request.urlretrieve(url2, f)


def html_url2(url):
    url2 = []
#     f = urllib3.PoolManager()
# #然后你需要一个PoolManager实例来生成请求,由该实例对象处理与线程池的连接以及线程安全的所有细节，不需要任何人为操作：
#     htmlur = f.request('GET', url, headers=heads
    f = urllib.request.Request(url, headers=heads)
    html_connect = urllib.request.urlopen(f).read()
    html_connect = html_connect.decode('utf-8', 'ignore')
    r = re.compile('"BDE_Image" src="(.*?)"')
    html_connect2 = re.findall(r, html_connect)
    #过滤广告图片
    for i in html_connect2:
        if i.endswith('.png'):
            continue
        url2.append(i)
    return url2


def html_url(url):
    html = []
    f = urllib.request.Request(url, headers=heads)
    html_connect = urllib.request.urlopen(f).read()
    html_connect = html_connect.decode('utf-8')
    r = re.compile('rel="noreferrer" href="(.*?)"')
    uname = re.findall('<title>(.*?)</title>', html_connect)
    html_url2 = re.findall(r, html_connect)
    for i in html_url2:
        if i == "#":
            continue
        html.append(i)
    return html, uname




if __name__ == "__main__":
    f, name = html_url("https://tieba.baidu.com/f?fr=wwwt&kw=%E4%B8%9D%E8%A2%9C")
    f = set(f)
    iq = 1
    for i in f:
        if i.endswith('p', 1, 2):
            fa = html_url2(tieba + i)
            cd = len(fa)
            for b in fa:
                img_down(b, name, cd)
            #print(i)
        # if iq == 1:
        #     break