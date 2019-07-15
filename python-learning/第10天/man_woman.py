import random

man = 1000
woman = 1000

#0正1负
def sj(man_gl, woman_gl):
    global man, woman
    if man_gl == 0:
        print("男人出的是正面")
    else:
        print("男人出的是反面")
    if woman_gl == 0:
        print("女人出的是正面")
    else:
        print("女人出的是反面")
    if man_gl == 0 and woman_gl == 0:
        man += 1
        woman -= 1
    elif man_gl == 1 and woman_gl == 1:
        man += 3
        woman -= 3
    else:
        woman += 2
        man -= 2
    print("男人的金钱为%d" % man)
    print("女人的金钱为：%d" % woman)
    return man, woman
if __name__ == "__main__":
    for i in range(100):
        man_gl = random.randint(0, 1)
        woman_gl = random.randint(0, 1)
        #woman_gl = 1
        man_jq, woman_jq = sj(man_gl, woman_gl)
