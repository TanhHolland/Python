x = int(input())
def check(a,b) :
    a.sort()
    b.sort()
    for i in range(0,n) :
        if a[i] > b[i] : return "NO"
    return "YES"
while x > 0:
    x-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(check(a,b))
    