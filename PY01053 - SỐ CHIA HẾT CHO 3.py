import math
x = int(input())
def snt(n) :
    if n < 2 : return False
    a = math.sqrt(n)
    a = int(a)
    for i in range(2,a+1):
        if n % i == 0: return False
    return True
def check(n):
    sum = 0
    for i in n:
        a = int(i)
        sum += a
    if(sum%3 == 0) :return "YES"
    return "NO"
while x > 0:
    x-=1
    n = input()
    print(check(n))
    