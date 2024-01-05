t = int(input())
while t>0:
    t-=1
    n = int(input())
    dem = 0
    i = 1
    while i*(i+1) < 2*n :
        res = (n*1.0 - i*(i+1)/2) /(i+1)
        if res == int(res) :
            dem+=1
        i+=1
    print(dem)