#def calc_sum(*agrs):
#    def sum():
#        ax = 0
#        for i in agrs:
#            ax = ax + i
#        return ax
#    return sum
#闭包
#def count():
#    def f(j):
#        def g():
#            return j*j
#        return g
#    fs = []
#    for i in range(1,4):
#        fs.append(f(i))
#    return fs

def createcounter():
    i = [0]
    def g():
        i[0] += 1
        return i[0]
    return g
