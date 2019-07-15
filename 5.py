# -*- coding: utf-8 -*-

def triangles():
    # 前两行无规律
    L = [1]
    yield L
    L = [1, 1]
    yield L
    # 从第三行开始
    layer = 3
    while True:
        Ln = []
        for i in range(layer):
            # 第一个为1
            if i == 0:
                Ln.append(1)
                print(layer)
            # 中间使用上次结果进行计算
            elif i < layer - 1:
                Ln.append(L[i-1] + L[i])#L
            # 最后一个为1
            else:
                Ln.append(1)
        yield Ln
        L = Ln
        layer += 1
