n, m, k = list(map(int, input().split()))
a = [[] for _ in range(n+1)]
vi = [0] * (n+1)
for _ in range(m):
    x, y = list(map(int, input().split()))
    a[x].append(y)
    a[y].append(x)

def DFS(u: int):
    vi[u] = 1
    for i in a[u]:
        if vi[i] == 0:
            DFS(i)


DFS(k)
for i in range(1, n+1):
    if vi[i] == 0:
        print(i)
