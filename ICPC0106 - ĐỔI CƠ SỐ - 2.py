import math
x = int(input())
def tinhchuoi(xau,n):
    sum = 0
    lst = list(xau)
    lst = map(int, lst)
    for i in lst:
        sum = sum*2 + i
    if sum == 10: return "A"
    elif sum == 11: return "B"
    elif sum == 12: return "C"
    elif sum == 13: return "D"
    elif sum == 14: return "E"
    elif sum == 15: return "F"
    return str(sum)
def kqua(s,n):
    if n == 1: return s
    while len(s) % n != 0:
        s = "0" + s
    kq = ""
    for i in range(0, len(s)-n+1, n):
        xau = s[i:i+n]
        kq += tinhchuoi(xau,n)
    return kq
while x > 0:
    x -= 1
    n = int(input())
    s = input()
    n = int(math.log(n,2))
    print(kqua(s,n))


