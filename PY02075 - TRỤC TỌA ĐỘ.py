# n,k = list(map(int,input().split()))
t = int(input())
ds = []
for _ in range(t) :
    n = int(input())
    for _ in range(n) :
        s = list(map(int,input().split()))
        ds.append((s[0],s[1]))
    ds = sorted(ds,key= lambda x : (x[1],x[0]))
    dem = 1
    pos = ds[0][1]
    for i in range(1,n) :
        if ds[i][0] >= pos :
            pos = ds[i][1]
            dem+=1
    # print(ds)
    ds.clear()
    print(dem)