# 5
# 18 27 16 22 6
# 5, 7, 5, 6, 2
n = int(input())
a = list(map(int,input().split()))
i = 1
while True:
    b = [i]*n
    check = True
    i+=1
    for j in range(0,n-1) :
        b[j+1] = int(b[j]*a[j+1]/a[j])
    heso = a[0]//b[0]
    for j in range(1,n) :
        if b[j] == 0 : b[j] +=1
        while a[j] // b[j] > heso :
            b[j] += 1
        if a[j] // b[j] < heso :
            check = False
    if check == True :
        print(sum(b))
        break
        