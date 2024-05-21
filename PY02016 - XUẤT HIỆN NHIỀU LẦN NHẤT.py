import math
import collections
x = int(input())
while x > 0:
    x-=1
    n = input()
    a = list(map(int,input().split()))
    d = {}
    res = -1
    kq = 0
    for i in a :
        if i not in d :
            d[i] = 1
        else :
            d[i] += 1
    for key in d.keys():
        if d[key] > res :
            res = d[key]
            kq = key
    if len(a)//2 < res : 
        print(kq)
    else: print("NO")