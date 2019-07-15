#使用 Python 生成类似于字母验证码图片
#需要用到的函数以及使用方法在random.py文件
#string方法在string.py文件
import random
import string
from PIL import Image,ImageFont,ImageDraw

lete = ''.join([random.choice(string.ascii_letters) for i in range(4)])
print(lete)
width = 100
height = 40
# for x in range(height):
#     for y in range(width):
#         print("现在的坐标是：(%d,%d)" % (x, y))
im = Image.new("RGB", (width, height), (255, 255, 255))
dr = ImageDraw.Draw(im)
zt = ImageFont.truetype("arial.ttf", 15)

for i in range(4):
    dr.text((15+i*20, 15), lete[i], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), zt)

for x in range(width):
    for y in range(height):
#        im.getpixel(x, y)
        if im.getpixel((x, y)) == (255, 255, 255):
            im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
  #      im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))



im.show()

#a = random.('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
