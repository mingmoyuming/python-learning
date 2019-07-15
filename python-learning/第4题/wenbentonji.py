#任一个英文的纯文本文件，统计其中的单词出现的个数。
import re

# f = open(r'E:\mysql.txt','r',encoding='utf-8')
# str = f.read()
#
# reobj = re.compile("\b?([a-zA-Z]+)\b?")
# words = reobj.findall(str)
#
# word_dict = {}
#


# import re
import os
from pprint import pprint

path = "E:\mysql.txt"


def wordstat(path):
    f = open(path, 'r+',encoding="utf-8")#打开
    wordcount = {}
    # t = f.read().split()
    # for i in t:
    #     print(i)
    for t in re.sub('[^0-9a-zA-Z]+', " ", f.read()).split():
        if t not in wordcount:
            wordcount[t] = 1
        else:
            wordcount[t] += 1
    print(wordcount)


if __name__ == '__main__':
    wordstat('E:\mysql.txt')