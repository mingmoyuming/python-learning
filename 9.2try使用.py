#9.2
try:
    f = open('administearot.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print("文件打开或是文件名字错了，需要重新修改，希望能测试成功吧!:"+str(reason))
except TypeError as reason:
    print("文件名不纯在的："+ str(reason))
