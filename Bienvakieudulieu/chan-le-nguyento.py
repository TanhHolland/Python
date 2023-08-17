import math
x = int(input())
def snt (a):
    if a < 2: return False
    n = math.sqrt(a)
    n = int(n)
    for i in range(2,n+1):
        if a %i ==0: return False
    return True
def check(n):
    sum = 0
    for i in range(0,len(n)):
        c = int(n[i])
        if (i % 2 == 1 and c % 2 == 0): return "NO"
        if (i % 2 == 0 and c % 2 == 1): return "NO"
        sum+=c
    if(snt(sum) == False): return "NO"   
    return "YES"
while x > 0:
    x-=1
    n = input()
    print(check(n))
    