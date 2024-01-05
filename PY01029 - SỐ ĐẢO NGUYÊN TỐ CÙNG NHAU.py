from math import gcd
x = input()
x = int(x)
while x > 0 :
    x-=1
    s = input()
    lst = list(s)
    lst.reverse()
    xau = "".join(lst)
    a = int(s)
    b = int(xau)
    if(gcd(a,b) == 1): print("YES")
    else: print("NO")