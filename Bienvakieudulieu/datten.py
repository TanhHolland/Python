a,b = list(map(int,input().split()))
s = set(input().split())
s = list(s)
s.sort()
n = len(s)
visited = [0]*(n+1)
xau = []
def Try(pos,b,s,xau) :
    for i in range(pos,len(s)) :
        if visited[i] == 0:
            visited[i] = 1
            xau.append(s[i])
            if len(xau) == b :
                for j in xau :
                    print(j,end=" ")
                print()
            else : Try(i+1,b,s,xau)
            visited[i] = 0
            xau.pop()
Try(0,b,s,xau)