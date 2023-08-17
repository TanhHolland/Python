import math
x = int(input())
def snt(a):
    if a < 2 : return False
    n = math.sqrt(a)
    n = int(n)
    for i in range(2,n+1) :
        if a %i == 0: return False
    return True
def check(n):
    # dict = {}
    dem = len(n)
    demsnt = 0
    for i in n:
        a = ord(i)
        if snt(a) : demsnt+=1
    if(snt(dem) == True and demsnt > dem - demsnt) :return "YES"
    return "NO"
while x > 0:
    n = input()
    x-=1
    print(check(n))
    