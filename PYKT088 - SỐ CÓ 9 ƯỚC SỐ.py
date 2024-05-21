import math


def Try(n: int) -> int:
    a = [i for i in range(math.isqrt(n) + 1)]
    for i in range(2, math.isqrt(n) + 1):
        if a[i] == i:
            for j in range(i*2, math.isqrt(n) + 1, i):
                if a[j] == j:
                    a[j] = i
    dem = 0
    for i in range(2, math.isqrt(n) + 1):
        p = a[i]
        q = a[i//p]
        if p*q == i and q != 1 and p != q:
            dem += 1
        elif a[i] == i:
            if i**8 <= n:
                dem += 1
    return dem


print(Try(int(input())))
