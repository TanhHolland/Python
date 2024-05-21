t = int(input())
dinh = 0
dem = 1
def DFS(u : int) :
    global a,vi
    vi[u] = 1
    for i in a[u] :
        if vi[i] == 0 :
            DFS(i)
def tinhLienThong() :
    global vi,n,dem,dinh
    for i in range(1,n+1) :
        vi = [0]*(n+1)
        vi[i] = 1
        d = 0
        for j in range(1,n+1) :
            if vi[j] == 0:
                DFS(j)
                d+=1
        if d > dem :
            dem = d
            dinh = i
while t >0 :
    t-=1
    n,m = list(map(int,input().split()))
    a = [[] for _ in range(n+1)]
    for _ in range(m) :
        x,y = list(map(int,input().split()))
        a[x].append(y)
        a[y].append(x)
    dinh = 0
    dem = 1
    tinhLienThong()
    print(dinh)    