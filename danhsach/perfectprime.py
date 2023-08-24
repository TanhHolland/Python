import math
def snt(n) :
    if n < 2 : return False
    if n <=3 : return True
    if n%2 == 0 or n%3 == 0: return False
    kq = int(math.sqrt(n))
    i = 5
    while i <= kq :
        if n%i == 0 or n%(i+2) == 0 : return False
        i+=6
    return True
def check(n):
    if snt(int(n)) == False or snt(int(n[::-1])) == False : return "No" 
    n = int(n)
    sum = 0
    while n > 0:
        temp = n % 10
        if snt(temp) == False:
            return "No"
        sum+=temp
        n //= 10
    if snt(sum) == False: return "No"
    return "Yes"
x = int(input())
while x > 0:
    x -= 1
    n = input()
    print(check(n))
