def digui(n):
    if n == 1:
        return 1
    else:
        return n * digui(n-1)

    
a = int(input('请输入一个整数:'))
result = digui(a)
print("%d的阶乘是:%d"% (a,result))
