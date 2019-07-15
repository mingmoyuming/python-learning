# -*- coding: utf-8 -*-

def findminandmax(L):
    if L == []:
        return (None,None)
    else:
        max = L[0]
        min = L[0]
        for m in L:
            if m < min:
                min = m
            if m > max:
                max = m
    return min,max
