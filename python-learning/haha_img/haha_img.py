#hahamax爬虫解决方案

import urllib.request
import re
import os

header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
url = "https://www.hahamx.cn/good/day/"
def download_url(url):
    path = r"E:\python-learning\python-learning\haha_img\hahmax_img"
    try:
        os.chdir(path)
    except FileNotFoundError:
        os.mkdir(path)
        os.chdir(path)
    f = os.path.basename(url)
#    url_2 = url.replace("normal", "middle")
    urllib.request.urlretrieve(url, f)


def html_url(url):
    f = urllib.request.Request(url, headers=header)
    html_connect = urllib.request.urlopen(f).read()
    try:
        html_connect = html_connect.decode("GBK")
    except UnicodeDecodeError as e:
        html_connect = html_connect.decode("utf-8")
    r = re.compile('data-original="(//.*?)"')
    result = re.findall(r,html_connect)
    return result

if __name__ == "__main__":
    file = open("url_img.txt", 'w+', encoding='utf-8')
    for i in range(3):
        i += 1
        f = html_url(url+"%s" %i)
        for b in f:
            b = b.replace("normal", "middle")
            file.write("https:" + b + '\n')
            download_url("https:" + b)
        # print(f)
        # if i == 1:
        #     break
    # for i in f:
    #     file = download_url("https:" + i)
    file.close()