# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
# -*- coding: utf-8 -*-

import os
#import string
import re
import pprint


# for i in path:
#     if os.path.splitext(i)[1] == '.py':

def statisics(name):
    fh = open(name, 'r', encoding="utf-8")
    read_fh = fh.readlines()
    fh.close()
    statisics_Comment = 0
    statisics_air = 0
    statisics_row = 0
    c = 0
    pattern = '.*#'  # 正则匹配模式
    for x in read_fh:
        if '#' in x:  # 计算注释数目
            if re.findall(pattern,x)[0][:-1].isspace() or re.findall(pattern,x)[0][:-1]=='':
                statisics_Comment += 1
                c = c+1
            else:
                statisics_row += 1
                c = c + 1
        elif x.isspace():
            statisics_air += 1
            c = c + 1
        else:
            statisics_row += 1
            c = c + 1
    return statisics_Comment, statisics_air, statisics_row,c


if __name__ == '__main__':
    os.chdir(r'E:\python-Actual-combat')
    path = os.listdir()
    for i in path:
        if os.path.splitext(i)[1] == '.py':
            a, b, c, d = statisics(i)
            print("文件:%s,注释:%d"%(i,a))
            print("文件:%s,空格:%d"%(i,b))
            print("这个不知道是什么%d"%c)
            print("文件:%s,行数:%d"%(i,d))


# fh=open('statistics_test.py', 'r', encoding="utf-8")
# read_fh=fh.readlines()
# fh.close()
# number_code=0
# number_empty=0
# number_note=0
# pattern='.*#' #正则匹配模式
# c = 0
#
# for x in read_fh:
#     if '#' in x: #计算注释数目
#         if re.findall('.*#',x)[0][:-1].isspace() or re.findall('.*#',x)[0][:-1]=='':
#             number_note += 1
#            # print(x)
#             c += 1
#         else:
#             number_code += 1
#             c += 1
#             print(x)
#
#     elif x.isspace():
#         number_empty += 1
#         c += 1
#         # print(x)
#     else:
#         number_code+=1
#         c += 1
#     #if c == 1:
#      #   break
#        # print(x)
# print('code number is %d'%(number_code+number_empty+number_note))
# print('empty number is %d'%number_empty)
# print('note number is %d'%number_note)
# #print("你写了%d行代码"%c)
