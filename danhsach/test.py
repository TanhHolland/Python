import math
while True :
    s = list(map(int,input().split()))
    if s.count(0) == 4 : break
    dem = 0
    while s.count(s[0]) != 4 :
        s.append(abs(s[0] - s[1]))
        dem+=1
        del s[0]
    print(dem)
