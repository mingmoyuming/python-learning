def digui(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
a = int(input('请输入一个整数:'))
result = digui(a)
print("%d的阶乘是:%d"% (a,result))
