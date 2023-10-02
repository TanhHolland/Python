def check(a,m,s : str) :
    if a < len(s) :
        return 0
    if a == len(s) : 
        return 1
    n = a - len(s) + 1
    if len(set(list(s))) > 1 :
        result = n % m
        for i in range(n - 1):
            result = (result * 26) % m
        return result
        # return n%m*(26**(n-1)% m) %m
    else :
        result = (25**(n-1)) % m
        for i in range(1, n):
            result = (result + (i * 26**(n-1))) % m
        return result
        # return 25**(n-1)%m + (n-1)% m*(26**(n-1)% m) % m
t = int(input())
for _ in range(t) :
    a,m = list(map(int,input().split()))
    s = input()
    print(check(a,m,s))