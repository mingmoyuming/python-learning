#9.5
try:
   
    sum = 1 + '1'
    f = open('我又是一个不存在的文档')
    print(f.read())
    f.close
except (OSError,TypeError):
    print("文档出错了，出错原因大概是："+ str(reason))
