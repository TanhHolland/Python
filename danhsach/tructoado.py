t = int(input())
while t > 0:
    t-=1
    n = int(input())
    lst = []
    while n > 0:
        n-=1
        a,b = list(map(int,input().split()))
        cap = (a,b)
        lst.append(cap)
    lst = sorted(lst,key= lambda x : (x[1],x[0]))
    dem = 0
    diemcuoi = 0
    for i in lst :
        if i[0] >= diemcuoi :
            diemcuoi = i[1]
            dem+=1
    print(dem)
    # print(lst)