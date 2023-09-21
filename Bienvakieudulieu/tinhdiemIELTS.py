x = int(input())
def ktra(a,b,n) :
    if a <= n and n <= b : return True
    return False 
def check(n : int) :
    if ktra(39,40,n):
        return 9.0
    if ktra(37,38,n):
        return 8.5
    if ktra(35,36,n):
        return 8.0
    if ktra(33,34,n):
        return 7.5
    if ktra(30,32,n):
        return 7.0
    if ktra(27,29,n):
        return 6.5
    if ktra(23,26,n):
        return 6.0
    if ktra(20,22,n):
        return 5.5
    if ktra(16,19,n):
        return 5.0
    if ktra(13,15,n):
        return 4.5
    if ktra(10,12,n):
        return 4.0
    if ktra(7,9,n):
        return 3.5
    if ktra(5,6,n):
        return 3.0
    if ktra(3,4,n):
        return 2.5
    else : 
        return 2.0
def lamtron(kq) :
    sauphay = kq - int(kq)
    nguyen = int(kq)
    if sauphay >=0.75 : return float(nguyen)  + 1
    elif sauphay >= 0.25 : return float(nguyen) + 0.5
    else : return float(nguyen) 
while x > 0:
    x-=1
    a,b,c,d = list(map(float,input().split()))
    a = check(a)
    b = check(b)
    tb = (a+b+c+d) /4
    print(lamtron(tb))
    