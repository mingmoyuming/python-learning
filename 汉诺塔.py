def hannoi(n,x,y):
    if n == 1:
            print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        haonoi(n-1,y,x,z)
n = int(input('请输入汉诺塔的层数:'))
hannoi(n,'X','Y','Z')
