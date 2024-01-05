import math
x = input()
x = int(x)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def check(a):
    if a < 2:
        return False
    n = math.sqrt(a)
    n = int(n)
    for i in range(2, n+1):
        if a % i == 0:
            return False
    return True


while x > 0:
    x -= 1
    a, b = input().split()
    a = int(a)
    b = int(b)
    uc = gcd(a, b)
    sum = 0
    while (uc > 0):
        sum += uc % 10
        uc = int(uc/10)
    if check(sum) == True:
        print("YES")
    else:
        print("NO")
