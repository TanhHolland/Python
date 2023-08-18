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
    s = s[len(s)-4:]
    s = int(s)
    if snt(s):
        return "YES"
    return "NO"
while x > 0:
    x -= 1
    s = input()
    print(check(s))
