# from PIL import Image,ImageDraw,ImageFont
#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# def add_run(image):
#     draw = ImageDraw.Draw(image)
#     myfont = ImageFont.truetype('C:\Windows\Fonts\simhei.ttf',size=40)
#     fontcolor = "#FF0000"
#     width,height = image.size
#     print(width,height)
#     draw.text((width-99, 0), '99', font=myfont, fill=fontcolor)
#     image.save('E:\\resulit.png','png')
#
#
# if __name__ == "__main__":
#     image = Image.open('E:\\tx.png')
#     add_run(image)

from PIL import Image, ImageDraw, ImageFont

def add_run(imaes):
    draw = ImageDraw.Draw(imaes)    #创建一个可以在给定图像上绘图的对象。
    # print(draw)
    width, heighy = imaes.size
    #draw.text((width-50,0),'1',fill="#FF0000")
    # draw.line((0,heighy, width, 0), fill = "#FF0000")#绘画对角线
    # draw.line((0, 0, width, heighy),width = 128 , fill="#FF0000")
#    draw.arc((0,0,200,200),0 ,90 ,fill="#FF0000") #在给定的区域内，在开始和结束角度之间绘制一条弧（圆的一部分）
    myfont = ImageFont.truetype('C:\Windows\Fonts\STXINGKA.ttf', size=10)
    wz = "尊敬的顾客你好，我是你爹。"
    draw.text((width-160, 0), wz, fill="#FF0000", font=myfont)
    imaes.show()
    imaes.save(r'E:\resulit.png', 'png')


if __name__ == "__main__":
    img = Image.open(r'E:\tx.png')
    print(img)
    add_run(img)






# def run(text):
#     a = []
#     while True:
#         a.append(text)
#         if len(a) == 1020:
#             d = "".join(map(lambda  x:str(x),a))
#             print(d)
#             break
#
# if __name__ == "__main__":
#     run("e")