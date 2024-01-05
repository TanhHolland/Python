# n,k = list(map(int,input().split()))
t = int(input())
for _ in range(t) :
    n = int(input())
    x,y,z = list(map(int,input().split()))
    f = [0]*(n+1)
    f[1] = x
    for i in range(2,n+1) :
        f[i] = f[i-1] + x
        if i % 2 == 0 :
            f[i] = min(f[i//2] + z,f[i])
        else :
            f[i] = min(f[i],f[i//2 + 1] + y + z)
    print(f[n]) 