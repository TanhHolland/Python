a,b,m = list(map(int,input().split()))
def ktrathuanngich(number,m) :
    s = ""
    while number > 0 :
        sodu = number % m
        s = str(sodu) + s
        number //= m
    return s == s[::-1]
dem = 0
for i in range(a,b+1) :
    check  = True
    for j in range(2,m+1):
        if not ktrathuanngich(i,j) :
            check = False
            break
    if check:
        dem+=1
print(dem)