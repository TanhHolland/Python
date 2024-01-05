t = int(input())
mod = 10**9 + 7
while t > 0 :
    t-=1
    n,k = list(map(int,input().split()))
    s,p = 0,1
    while k > 0:
        if k % 2 == 1 :
            s += p
            s %= mod
        p *= n
        k//=2
    print(s)