def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)


test = int(input())
while test > 0:
    test -= 1
    n,k = list(map(int, input().split()))
    s = []
    while len(s) < n:
        s+= list(map(int, input().split()))
    kt = n+1
    for i in range(n):
        x = s[i]
        for j in range(i, n):
            if ucln(s[j], x) == k:
                kt = min(kt, j-i+1)
                break
            if ucln(s[j], x) < k:
                break
    if kt < n+1:
        print(kt)
    else:
        print(-1)
