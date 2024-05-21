n = int(input())
a = [[] for _ in range(n+1)]
for _ in range(n-1) :
    x,y = list(map(int,input().split()))
    a[x].append(y)
    a[y].append(x)
d1,d2 = 0,0
for i in range(1,n+1):
    if len(a[i]) == 1 : d1+=1
    if len(a[i]) == n-1 : d2+=1
if d1 + d2 == n :
    print("Yes")
else :
    print("No")