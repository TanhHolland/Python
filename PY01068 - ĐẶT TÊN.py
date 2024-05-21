# n,k = input().split()
# n,k = int(n),int(k)
# s = [int(x) for x in input().split()]
# ds = []
# for i in s:
#     if i not in ds :
#         ds.append(i)
# ds.sort()
import queue
a, b = list(map(int, input().split()))
s = set(input().split())
s = list(s)
s.sort()
n = len(s)
visited = [0]*(n+1)
xau = []


def Try(pos):
    if len(xau) == b:
        print(" ".join(xau))
        return
    for i in range(pos,n):
        if visited[i] == 0:
            visited[i] = 1
            xau.append(s[i])
            Try(i+1)
            visited[i] = 0
            xau.pop()

Try(0)
