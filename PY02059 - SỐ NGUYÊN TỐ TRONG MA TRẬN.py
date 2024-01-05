n, m = map(int,input().split()) 
t = n
MAX = 1005
a = [0]*MAX
for i in range(2,MAX//2+1) :
    if a[i] == 0:
        for j in range(i*2,MAX,i) :
            if a[j] == 0:
                a[j] = 1
kq = -1
ds = []
while t > 0:
    t-=1
    s = list(map(int,input().split()))
    ds.append(s)
    for i in s :
        if a[i] == 0:
            kq = max(i,kq)
if kq == -1 : 
    print("NOT FOUND")
else :
    print(kq)
    for i in range(len(ds)) :
        for j in range(len(ds[i])) :
            if ds[i][j] == kq :
                print("Vi tri [{}][{}]".format(i,j))