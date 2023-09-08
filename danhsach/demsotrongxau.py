x = int(input())
while x > 0:
    x-=1
    s = input()
    k = input()
    dem = 0
    pos = 0
    while (s.find(k,pos) != -1) :
        dem += 1
        pos = s.find(k,pos) + len(k)
    print(dem)