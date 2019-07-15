# -*- coding:utf-8 -*-
#0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import  random
import string
import MySQLdb
import pymysql
import uuid


print(uuid.uuid1())
# db = MySQLdb.connect("47.106.203.183","root","aA123.com","bysj")

# def rande(prefix,length):
#     s = []
#     for i in prefix:
#         s.append(i)
#     while True:
#         if len(s) > length:
#             break
#         f = string.ascii_letters
#         r = random.choice(f)
#         s.append(r)
#     return s
#
# if __name__ == "__main__":
#     b = 0
#     while True:
#         if b == 200:
#             break
#         a = rande("",25)
#         d = "".join(map(lambda x:str(x),a))
#         print("第 %s 个:" %(b+1) ,d)
#         b = b + 1