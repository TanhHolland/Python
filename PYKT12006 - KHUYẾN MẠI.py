import re
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = []
for i in range(len(a)) :
    d.append((a[i],b[i],a[i]-b[i]))
d = sorted(d,key = lambda x : (x[2]))
tien = 0
for i in range(n) :
    if k > 0 :
        k-=1
        tien += d[i][0]
    else :
        tien += min(d[i][0],d[i][1])
print(tien)