import math
x = int(input())
def snt(a):
    if a < 2:
        return False
    n = math.sqrt(a)
    n = int(n)
    for i in range(2, n+1):
        if a % i == 0:
            return False
    return True
def check(s):
    s1 = 0
    s2 = 0
    for i in s:
        num = int(i)
        if snt(num): s1 += 1
        else : s2 += 1
    if snt(len(s)) and s1 > s2:
        return "YES"
    return "NO"
while x > 0:
    x -= 1
    s = input()
    print(check(s))