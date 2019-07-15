#用 Python 写一个爬图片的程序。爬：http://tieba.baidu.com/f?kw=%E6%9D%89%E6%9C%AC%E6%9C%89%E7%BE%8E

import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import os

# file = open('html.txt', 'w+', encoding='utf-8')
# #encoding=utf-8
# cookies = '''AIDUID=2705347F00960B26BC03BC60EDF6BFD7:FG=1; BIDUPSID=2705347F00960B26BC03BC60EDF6BFD7; PSTM=1555653669; HOSUPPORT=1; delPer=0; PSINO=7; ZP_FR=aladdin-5463-zp_exact_new; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; pplogid=1539htdaAZictUTD0D%2F8xOu%2FIwzIYV0yn%2BxGogjoRvZ%2BRUDMDcfgJdU15xHKYAzNF3GrpJpXwqrGcKCbdm2xNuDLlw%3D%3D; UBI=fi_PncwhpxZ%7ETaJc9rlSgMGljwKsilWcg1rXpi1k6KDYzXJTZmVI90Y5wZSJ-oZF8M2b8alfnRGLWPylB5N; STOKEN=5400f999bb37abcb8483a7df0d1903e1ad3778afc6a145124d7237ff99fc091a; USERNAMETYPE=1; SAVEUSERID=464e76ecb0be389b28e20db085; BDUSS=U8zbHZBREJnaDBEcFdTNUY4YTJqY0VpUXpJck1sczEtT0F-cEE3MzEwLW5JUnhkSVFBQUFBJCQAAAAAAAAAAAEAAAD5Oy9jx-C1wLS0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKeU9FynlPRcU; PTOKEN=1eaeb9fecebcbd2d293043115cf02198; HISTORY=dad1f6492ad5e70365761a44ebdef247eac775da55080c9b548d; Cuid=2705347F00960B26BC03BC60EDF6BFD7%3AFG%3D1; Appid=tieba; Appkey=appkey; DeviceType=20; Extension-Version=2.2; LCS-Header-Version=1; H_PS_PSSID=26525_1428_21118_18559_29135_20697_28518_29099_29139_29134_28834_28584_29133_20719'''
# heasd = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Connection': 'keep-alive', 'Accept': '*/*' ,'Cookie':cookies }
# url = "https://tieba.baidu.com/f?fr=wwwt&kw=008"
# wbad = requests.get(url, headers=heasd)
# wbad.encoding='utf-8'
# soup = BeautifulSoup(wbad.text, 'lxml')
# file.write(wbad.text)
# #soup = soup.encode('utf-8')
# # for i in soup:
# #     m += 1
# #     if m == 1:
# #         continue
# #     print(i)
# file.close()
#

url2 = "http://imgsrc.baidu.com/forum/pic/item/"

def html_down(pathname):
    path = r"E:\a small program every day\第13天\image"
    try:
        os.chdir(path)
    except FileNotFoundError as e:
        os.mkdir(path)
        os.chdir(path)
    f = os.path.basename(pathname)
    # r = re.findall('(...\.)', url)
    # print(r)
    urllib.request.urlretrieve(pathname, f)



def html_url(url):
    # file = open('html.txt', 'w+', encoding='utf-8')
    cookies = '''AIDUID=2705347F00960B26BC03BC60EDF6BFD7:FG=1; BIDUPSID=2705347F00960B26BC03BC60EDF6BFD7; PSTM=1555653669; HOSUPPORT=1; delPer=0; PSINO=7; ZP_FR=aladdin-5463-zp_exact_new; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; pplogid=1539htdaAZictUTD0D%2F8xOu%2FIwzIYV0yn%2BxGogjoRvZ%2BRUDMDcfgJdU15xHKYAzNF3GrpJpXwqrGcKCbdm2xNuDLlw%3D%3D; UBI=fi_PncwhpxZ%7ETaJc9rlSgMGljwKsilWcg1rXpi1k6KDYzXJTZmVI90Y5wZSJ-oZF8M2b8alfnRGLWPylB5N; STOKEN=5400f999bb37abcb8483a7df0d1903e1ad3778afc6a145124d7237ff99fc091a; USERNAMETYPE=1; SAVEUSERID=464e76ecb0be389b28e20db085; BDUSS=U8zbHZBREJnaDBEcFdTNUY4YTJqY0VpUXpJck1sczEtT0F-cEE3MzEwLW5JUnhkSVFBQUFBJCQAAAAAAAAAAAEAAAD5Oy9jx-C1wLS0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKeU9FynlPRcU; PTOKEN=1eaeb9fecebcbd2d293043115cf02198; HISTORY=dad1f6492ad5e70365761a44ebdef247eac775da55080c9b548d; Cuid=2705347F00960B26BC03BC60EDF6BFD7%3AFG%3D1; Appid=tieba; Appkey=appkey; DeviceType=20; Extension-Version=2.2; LCS-Header-Version=1; H_PS_PSSID=26525_1428_21118_18559_29135_20697_28518_29099_29139_29134_28834_28584_29133_20719'''
    heasd = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 'Connection': 'keep-alive', 'Accept': '*/*' ,'Cookie':cookies }
    wbad = requests.get(url, headers=heasd)
    wbad.encoding = 'utf-8'
    #soup = BeautifulSoup(wbad.text, 'lxml')
    # file.write(wbad.text)
    # file.close()
    f = re.compile('data-original="(.*?)"')
    sad = re.findall(f, wbad.text)
    return sad


if __name__ == "__main__":
    f = html_url("https://tieba.baidu.com/f?fr=wwwt&kw=008")
    file = open('html.txt','w+',encoding='utf-8')
    for i in f:
        fa = os.path.basename(i)
        url3 = url2 + fa
        file.write(url3 + '\n')
        html_down(url3)
    file.close()