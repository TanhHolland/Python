t = int(input())
for _ in range(t) :
    n = int(input())
    a,b = [],[]
    for _ in range(n) :
        x,y = list(map(float,input().split()))
        a.append(x)
        b.append(y)
    f = [1] * (n+1)
    for i in range(n) :
        for j in range(i):
            if a[j] < a[i] and b[j] > b[i] :
                f[i] = max(f[i],f[j] + 1)
    print(max(f))
            