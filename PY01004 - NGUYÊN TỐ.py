from math import gcd
import math
t = int(input())
def ktra(a):
    if a < 2 : return False
    n = int(math.sqrt(a))
    for i in range(2,n+1):
        if(a % i == 0):
            return False
    return True
while(t > 0) :
    t-=1
    n = int(input())
    d = 0
    for i in range(1, n):
        if gcd(i,n) == 1: d += 1
    if(ktra(d)):
        print("YES")
    else:
        print("NO")