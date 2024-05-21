n, m = map(int,input().split()) 
t = n
MAXX = -1
MINN = 10005
ds = []
while t > 0:
    t-=1
    s = list(map(int,input().split()))
    ds.append(s)
    for i in s :
        MINN = min(MINN,i)
        MAXX = max(MAXX,i)
kq = MAXX - MINN
haha = []
check = False
for i in range(len(ds)) :
    for j in range(len(ds[i])) :
        if ds[i][j] == kq :
            check = True
            haha.append([i,j])
if check == False :
    print("NOT FOUND")
else :
    print(kq)
    for i in range(len(haha)) :
            print("Vi tri [{}][{}]".format(haha[i][0],haha[i][1]))