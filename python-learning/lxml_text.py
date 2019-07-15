from lxml import etree

def gethtml(html):
    return etree.HTML(html)

sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <a href="https//www.baidu.com">pageadmin</a>
    <!-- this is the end -->
  </body>
</html>
"""

s1 = gethtml(sample1)

#所有的值都是属于可迭代对象

# 获取文本内容用 text()
# 获取注释用 comment()
# 获取其它任何属性用@xx，如
# @href
# @src
# @value


# #2019年7月2日10:25:55 这简直就是神器啊
# print(s1.xpath('//title/text()'))#获取标题
# print(s1.xpath('/html/head/title/text()'))#也是获取标题
# print(s1.xpath('//h2/a/@src'))#h2地下获取src值
# print(s1.xpath('//@href')) #获取href值
# print(s1.xpath('//text()'))#获取所有的文本
# print(s1.xpath('//comment()')) #获取所有的注释



def getxpath(url):
    return etree.HTML(url)


sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""

s2 = getxpath(sample2)

#print(s2.xpath('//li[1]/text()'))#获取第一个
# print(s2.xpath('//li[position() = 1]/text()'))#同理
# print(s2.xpath('//li[position() mod2 = 1]/text()'))#获取所有基数的值
# print(s2.xpath('//li[position() mod2 = 0]/text()'))#获取偶数的值


sample3 = """<html>
  <body>
    <ul>
      <li id="begin"><a href="https://scrapy.org">Scrapy</a>begin</li>
      <li><a href="https://scrapinghub.com">Scrapinghub</a></li>
      <li><a href="https://blog.scrapinghub.com">Scrapinghub Blog</a></li>
      <li id="end"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
      <li data-xxxx="end" abc="abc"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
    </ul>
  </body>
</html>
"""
s3 = getxpath(sample3)

print(s3.xpath('//li/a["@href=https://scrapy.org"]/text()'))
print(s3.xpath('//li[@id="begin"]/a/text()'))
