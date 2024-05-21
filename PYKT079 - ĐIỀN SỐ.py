x = int(input())
while x > 0:
    x-=1
    n = int(input())
    a = list(map(int,input().split()))
    l = min(a)
    r = max(a)
    dem = 0
    for i in range(l,r+1):
        if a.count(i) == 0:
            dem+=1
    print(dem)