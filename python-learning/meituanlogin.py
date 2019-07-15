#
#登陆地址：https://passport.meituan.com/account/unitivelogin?risk_partner=0&risk_platform=1&risk_app=-1&uuid=3d21110326c44cf38e9d.1561535099.1.0.0&service=www&continue=https%3A%2F%2Fwww.meituan.com%2Faccount%2Fsettoken%3Fcontinue%3Dhttp%253A%252F%252Fwww.meituan.com%252F
import requests


def html_url(url):
    r = requests.get(url, timeout=10)
    html = r.text
    #html = html.encode('utf-8')
    print(html)


if __name__ == "__main__":
    f = html_url("https://www.baidu.com")
    # print(f)#

