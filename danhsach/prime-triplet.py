x = int(input())

def check(n):
    if n < 2: return False
    if n <=3: return False
    if n %2 == 0 or n%3 == 0: return False
    i = 5
    while i * i <=n :
        if n %i == 0 or (n+2) %i == 0 : return False
        i+=6
    return True
while x > 0:
    x -= 1
    n = int(input())
    c = 0
    for i in range(2,n-6) :
        if (check(i) and check(i+2) and check(i+6)) or (check(i) and check(i+4) and check(i+6)) : c+=1
    print(c)
        