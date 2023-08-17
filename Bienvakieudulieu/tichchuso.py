import math
x = int(input())
def check(n):
    sum = 1
    for i in n:
        a = int(i)
        if a!= 0: sum *= a
    return sum
while x > 0:
    x-=1
    n = input()
    print(check(n))
    