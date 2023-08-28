x = int(input())
while x > 0:
    x-=1
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    c = True
    for i in range(0,n):
        if a[i] > b[i] : c = False
    if c == True : print("YES")
    else : print ("NO")