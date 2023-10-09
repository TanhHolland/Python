t = int(input())
while t > 0 :
    t-=1
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    a.sort()
    group = 0
    d = 0
    for i in a :
        if d + i <k :
            d+=i
        elif d +i == k :
            d = 0
            group+=1
        else :
            group += i//k
            d = i% k
    if d > 0 :
        group +=1
    print(group)