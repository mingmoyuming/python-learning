import urllib.request
import requests
import os


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



def down(url):
    path = r"E:\a small program every day\tup'
    try:
        os.chdir(path)
    except FileNotFoundError as e:
        os.mkdir(path)
        os.chdir(path)
