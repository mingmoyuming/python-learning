import re

file = open('result.txt', 'r', encoding='utf-8')
f = file.read()
f = re.findall('<p>(?:<.[^>]*>)</p>', f)
#f = set(f)
#result = re.findall('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>', html_content)
print(f)
file.close()

#https://blog.abczg.top/default/12.html