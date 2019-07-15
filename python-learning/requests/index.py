import requests
import urllib.request
import json

#head = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
head = {
    # ':authority': 'www.toutiao.com',
    # ':method': 'GET',
    # ':path': '/',
    # ':scheme': 'https',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'accept-language',
    # 'cache-control': 'max-age=0',
    # 'upgrade-insecure-requests': '1',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    'Referer': 'https://www.toutiao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
def html_url(url):
    # r = urllib.request.Request(url, headers=head)
    # f = urllib.request.urlopen(r)
    # #f = f.decode('utf-8')
    # print(f.read().decode('utf-8'))
    r = requests.get(url, headers=head).text
    data = json.loads(r) #将已编码的 JSON 字符串解码为 Python 对象
    #print(data)
    news = data['data']
    # print(news)
    for n in news:
        # print(n)
        title = n['title']
        # try:
        #     img_url = n['middle_image']
        # except KeyError:
        #     pass
        url = n['source_url']
        print("https://www.toutiao.com"+url, title)

    #print(bm)
#    print(r.text)
    #print(r.headers)



if __name__ == "__main__":
    url = "https://www.toutiao.com/api/pc/feed/"
    html_url(url)