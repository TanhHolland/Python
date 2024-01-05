t = int(input())
while t > 0 :
    t-=1
    n = int(input())
    s = list(map(int,input().split()))
    i = 0
    dem = 0
    while i < len(s)-1 :
        if max(s[i],s[i+1]) > 2 * min(s[i],s[i+1]) :
            s.insert(i+1,(max(s[i],s[i+1])+1)//2)
            dem+=1
        else : i+=1
    print(dem)