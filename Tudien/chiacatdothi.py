t = int(input())
dinh = 0
dem = 1
def DFS(u : int) :
    global a,visted
    visted[u] = 1
    for i in a[u] :
        if visted[i] == 0 :
            DFS(i)
def tinhLienThong() :
    global visted,n,dem,dinh
    for i in range(1,n+1) :
        visted = [0]*(n+1)
        visted[i] = 1
        d = 0
        for j in range(1,n+1) :
            if visted[j] == 0:
                DFS(j)
                d+=1
        if d > dem :
            dem = d
            dinh = i
for _ in range(t):
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