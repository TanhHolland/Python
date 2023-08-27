import math
while True :
    s = list(map(int,input().split()))
    if s.count(0) == 4 : break
    dem = 0
    while len(set(s)) > 1 :
        a = []
        for i in range(3) :
            a.append(abs(s[i] - s[i+1]))
        a.append(abs(s[3] - s[0]))
        dem+=1
        s = a
    print(dem)
