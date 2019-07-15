#一个HTML文件，找出里面的正文。

import urllib.request
import re
import urllib3.request

header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"}

def get_body(url):
    a = urllib.request.Request(url, headers=header)
    html_content = urllib.request.urlopen(a).read()
    #html_content = urllib.request.urlopen(url).read()
    try:
        html_content = html_content.decode('GBK')
    except UnicodeDecodeError as e:
        html_content = html_content.decode('utf-8')
   # print(html_content)
  #  r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    result = re.findall('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>', html_content)
    return result



if __name__ == '__main__':
    body = get_body('https://news.whu.edu.cn/info/1002/54111.htm')
    file_object = open('result.txt', 'w',encoding='utf-8')
    for l in body:
        file_object.write(l + '\n')
        print(l)
    file_object.close()







# from urllib import request
#
# head = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
#     'Accept-Encoding': 'gzip, deflate'
# }
#
# def get_body(url):
#     html_connetc = request.Request(url)
#     html_connetc.add_header(head)
#     html_connetc2 = request.urlopen(html_connetc)
#     r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
#     result = r.findall(html_connetc2.decode('GBK'))
#     return result
#
#
# if __name__ == "__main__":
#     body = get_body("https://news.whu.edu.cn/info/1002/54113.htm")
#     file = open('result.txt','w+')
#     for l in body:
#         file.write(l + '\n')
#     file.close()

# url = "https://news.whu.edu.cn/info/1002/54113.htm"
# a = urllib.request.Request(url)
# a.add_header("Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",'gzip, deflate')
# resone = urllib.request.urlopen(a)
# buff = resone.read()
# the_page = buff.decode("utf-8")
# r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
# result = r.findall(the_page)
# #file = open('result.txt', 'w+',encoding='utf-8')
# #file.write("%s "%the_page)
# print(result)
# file.close()