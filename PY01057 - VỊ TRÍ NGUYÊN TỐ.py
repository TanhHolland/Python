import math
x = int(input())
def snt (a) :
    if a < 2 : return False
    n = math.sqrt(a)
    n = int(n)
    for i in range(2,n+1) :
        if a %i == 0 : return False
    return True
def check (s) :
    for i in range(0,len(s)) :
        if (snt(i) == False) and (s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7'): return "NO"
        if (snt(i) == True) and (s[i] != '2' and s[i] != '3' and s[i] != '5' and s[i] != '7'): return "NO"
    return "YES" 
while x > 0:
    x-=1
    s = input()
    print(check(s))