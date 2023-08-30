def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)
x = int(input())
while x > 0:
    x -= 1
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))
    a = [1]*n
    check = False
    for i in range(1, n):
        j = i - 1
        while j >= 0 and ucln(s[i], s[j]) == k:
            a[i] += a[j]
            j -= a[j]
            check = True
    if check == True:
        print(max(a))
    else:
        ktra = False
        for i in s:
            if i % k == 0:
                ktra = True
        if ktra == False:
            print(-1)
        else:
            print(1)
