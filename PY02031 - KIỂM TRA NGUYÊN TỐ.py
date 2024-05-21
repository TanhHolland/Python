import math
def check(n : int) :
    if n < 2 : return False
    for i in range(2,int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

n,m = list(map(int,input().split()))
a = []
for _ in range(n) :
    a.append(list(map(int,input().split())))
for i in range(n) :
    for j in range(m) :
        if check(a[i][j]) == True :
            a[i][j] = 1
        else :
            a[i][j] = 0
for i in range(n) :
    for j in range(m) :
        print(a[i][j],end=' ')
    print()