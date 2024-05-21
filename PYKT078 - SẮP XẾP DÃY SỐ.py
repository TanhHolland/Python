x = int(input())
while x > 0:
    x-=1
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    MAX = max(a)
    pos = a.index(MAX)
    a.insert(pos,m)
    b = []
    c = []
    for i in a :
        if i < 0 :
            b.append(i)
        else :
            c.append(i)
    b.extend(c)
    for i in b :
        print(i,end=" ")
    print()