# -*- coding:utf-8 -*-
#
import os
import pprint
from PIL import ImageDraw,Image
import re
#IPHONE分辨率1136*640
'''
111
'''

iphone5_width=1136
iphone5_height=640
path = r'E:\a small program every day\第5天\sucai'
path2 = r'E:\a small program every day\第5天\wc'

def iphaone(path):
    c = 0
    for i in os.listdir(path):
      #  i = "v2-0a33a2a5ad7bdc038cc5fa683949ce08_r.jpg"
        a = os.path.join(path, i)
        # print(i.split('.')[0])
        #file = Image.open(a)
        with Image.open(a) as file:
            w, h = file.size
          #  print(file.size)
            n = w / 80 if (w / 80) >= (h / 80) else (h / 80) #0.70 if 0.95 >= 1.6875 else 2.4
         #   print(n)
         #   print((w/n),(h/n))
            file.thumbnail((w/n, h/n))#width 640 height 640
            #print(file.size)
            file.save(i.split('.')[0]+'.jpg') #注意，注意，保存只能保存在当前路径之下，无法保存在其他路径
           # c = c+1
          #  if c == 10:
           #     break

if __name__ == "__main__":
    iphaone(path)
# def change_resolution(path):
#     for picname in os.listdir(path):
#         picpath = os.path.join(path, picname)
#         with Image.open(picpath) as im:
#             w, h = im.size
#             n = w/1366 if (w/1366) >= (h/640) else h/640
#             im.thumbnail((w/n, h/n))
#             im.save(r'E:\a small program every day\第5天\wc',picname)
#
#
# if __name__ == '__main__':
#     change_resolution(path)