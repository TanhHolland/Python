while True :
    s = []
    check = True
    while len(s) < 2:
        x = list(map(int,input().split()))
        if -1 in x :
            check = False
            break
        s+=x
    if check == False : break
    s.sort()
    l = s[0]
    r = s[1]
    n = int(input())
    a = [0]*(r+1)
    for i in range(2,n+1) :
        x = l // i
        y = r // i
        for j in range(x,y+1):
            a[i*j] = 1
    dem = 0
    for i in range(l,r+1) :
        if a[i] == 0 :
            dem+=1
    print(dem)