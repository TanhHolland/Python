import math
n = int(input());
a = list(map(int,input().split()))
p = 0
dict = {}

def tinhTongCacUoc(n : int) :
    sum = 1 + n
    m = int(math.sqrt(n))
    if m * m == n :
        sum += m
    else :
        m += 1
    for i in range(2,m) :
        if (n % i) == 0 :
            sum += i + (n // i)
    return sum

for i in range(len(a)) :
    left = 0
    right = 0
    for j in range(0, i) :
        if a[j] > a[i] :
            left +=1
    for j in range(i+1, len(a)) :
        if a[j] < a[i] :
            right +=1
    if left*right > p :
        dict[a[i]] = left*right
        p = left*right
if(len(dict) > 0) :    
    for key in dict.keys() :
        print(tinhTongCacUoc(dict[key]),key)
        break
else :
    print("Neu khong co Thuong, Tai se buon biet may :(.")