n,m = list(map(int,input().split()))
a = []
MINN = 10005
MAXX = -1
for _ in range(n) :
    a.append(list(map(int,input().split())))
for i in range(n) :
    MINN = min(min(a[i]),MINN)
    MAXX = max(max(a[i]),MAXX)
d = MAXX - MINN
ds = []
check = False
for i in range(n) :
    for j in range(m) :
        if a[i][j] == d :
            check = True
            ds.append("Vi tri [{}][{}]".format(i,j))
if check == False :
    print('NOT FOUND')
else :
    print(d)
    for i in ds :
        print(i)