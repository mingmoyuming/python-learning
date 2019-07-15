import re


text = ''
file = open('poem.txt', 'r', encoding='GBK')

for i in file:
    text = text + i
file.close()
a = re.findall('你...', text)
a = set(a)
print(a)