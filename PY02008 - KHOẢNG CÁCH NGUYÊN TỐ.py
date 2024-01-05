import math
n,k = input().split()
n = int(n)
k = int(k)
MAXX = int(1e4)
a = [0]*MAXX
for i in range(2,MAXX//2 + 1) :
    if a[i] == 0 :
        for j in range(i*2,MAXX,i) :
            if a[j] == 0:
                a[j] = 1
kq = []
for i in range(2,MAXX) :
    if a[i] == 0:
        kq.append(i)
print(k,end=" ")
for i in range(0,n) :
    print(k + kq[i],end=" " )
    k+=kq[i]