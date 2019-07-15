# -*- coding:utf-8 -*-

# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import  random
import string


#def rande(prefix,length):

def rande(prefix,length):
    s = []
    for i in prefix:
        s.append(i)
    while True:
        if len(s) > length:
            break
        f = string.ascii_letters
        r = random.choice(f)
        s.append(r)
    return s

if __name__ == "__main__":
# s = string.ascii_letters
# r = random.choice(s)
    b = 0
    while True:
        if b == 200:
            break
        a = rande("",25)
        d = "".join(map(lambda x:str(x),a))
        print("第 %s 个:" %(b+1) ,d)
        b = b + 1

