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
# print(Try(int(input())))
# VD : số 36 có ước là : 1 2 3 4 6 9 12 18 36
# muốn 1 số có 9 ước --> số chính phương
# 1 6 36 là 3 ước --> còn lại 9-3 = 6 ước
# theo cách giải trên ta tìm p,q sao cho p*q = căn 36 (6)
# p = 2 , q = 3
# 36/p = 36/2 = 18 , 36/q = 36/3 = 12
# còn lại 6 - 4 = 2 ước
# lấy p^2 = 4, q^2 = 9 là 2 ước còn lại 
