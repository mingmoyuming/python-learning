#正则表达式训练
import re
import os
html_url = "http://b-ssl.duitang.com/uploads/item/201507/27/20150727185549_WisPY.jpeg"
f = re.findall('.*?(.*?\..*?)', html_url)
#print(f)
filename = os.path.basename(html_url)
print(filename)