#一个HTML文件，找出里面的链接

import urllib.request
import re
header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}
def get_http(url):
    a = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(a).read()
    html = html.decode('utf-8')
    b = re.findall('value="(.*?)"', html)
    return b
if __name__ == "__main__":
    for i in range(10):
        f = get_http(
            "https://suijimimashengcheng.51240.com/web_system/51240_com_www/system/file/suijimimashengcheng/get/?dx=true&xx=true&sz=true&fh=false&fh_value=!%40%23%24%2525%255E%26*&cd=16&ajaxtimestamp=1559035182713")
        file = open('result.txt', 'w+', encoding='utf-8')
        for i in f:
            file.write(i + '\n')
            print(i)
        file.close()