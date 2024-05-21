import math
x = int(input())
def check (a) :
    if (a < 2): return "NO"
    n = math.sqrt(a)
    n = int(n)
    for i in range(2,n+1):
        if a%i==0 : return "NO"
    return "YES"
while x > 0 :
    x-=1
    s = input()
    n = int(s[len(s)-4:])
    print(check(n))
    
    