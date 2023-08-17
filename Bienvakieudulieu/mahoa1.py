x = int(input())

while x > 0:
    x -= 1
    s = input()
    xau = " "
    dem = 0
    kq = ""
    for i in s:
        if i != xau:
            so = str(dem)
            kq +=  so + xau
            dem = 1
            xau = i
        else: 
            dem+=1
    so = str(dem)
    kq +=  so + xau
    print(kq[2:])

