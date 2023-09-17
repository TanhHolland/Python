x = int(input())
while x > 0:
    x-=1
    n = input()
    a = list(map(int,input().split()))
    dem = 0
    for i in range(1,len(a)-1) :
        l = 0
        r = len(a)-1
        checkAll = True
        while l < i and i < r :
            if l < i and a[l] <= a[i] :
                l+=1
            elif r > i and a[i] < a[r] :
                r-=1
            else:
                if l == r :
                    checkAll = False
        if checkAll == True :
            print(a[i])
            dem+=1
    ok1 = True
    for i in range(0,len(a)-1):
        if a[i] > a[-1] :
            ok1 = False
    if ok1 == True :
        dem+=1
    ok2 = True
    for i in range(len(a)-1,0,-1):
        if a[i] <= a[0] :
            ok2 = False
    if ok2 == True :
        dem+=1
                