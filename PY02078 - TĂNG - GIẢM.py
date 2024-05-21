# n,k = list(map(int,input().split()))
t = int(input())
for _ in range(t) :
    n = int(input())
    a = []
    b = []
    for _ in range(n) :
        s = list(map(float,input().split()))
        a.append(s[0])
        b.append(s[1])
    f = [1]*n
    for i in range(1,n) :
        for j in range(0,i) :
            if a[j] < a[i] and b[j] > b[i]:
                f[i] = max(f[i],f[j] + 1)
    print(max(f))
    
        