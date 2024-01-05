x = int(input())
ds = []
while len(ds) < x:
    ds += map(int,input().split())
a = []
b = []
for i in ds :
    if i %2 == 0:
        a.append(i)
    else :
        b.append(i)
a.sort()
b.sort(reverse=True)
p1 = 0
p2 = 0
for i in ds :
    if i %2 == 0:
        print(a[p1],end=" ")
        p1+=1
    else :
        print(b[p2],end=" ")
        p2+=1
