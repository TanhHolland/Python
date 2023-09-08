n, m = map(int,input().split()) 
t = n
kq = -1
ds = []
while t > 0:
    t-=1
    s = list(map(int,input().split()))
    ds.append(s)
    for i in s :
        i = str(i)
        j = i[::-1]
        if i == j and len(i) > 1:
            kq = max(kq,int(i))
if kq == -1 : 
    print("NOT FOUND")
else :
    print(kq)
    for i in range(len(ds)) :
        for j in range(len(ds[i])) :
            if ds[i][j] == kq :
                print("Vi tri [{}][{}]".format(i,j))