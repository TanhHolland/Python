import math
def check(a) :
    if a < 2 : return False
    n = int(math.sqrt(a))
    for i in range(2,n+1):
        if a%i == 0 :
            return False
    return True
n = int(input())
day = list(map(int, input().split()))
s = []
for i in day:
    if i not in s:
        s.append(i)
b = s.copy()
c = s.copy()
# print(s)
for i in range(1, len(b)):
    b[i] += b[i-1]
# print(b)
for i in range(len(c)-2, -1, -1):
    c[i] += c[i+1]
# print(c)
kq = -1
for i in range(0, len(s)-1):
    if check(b[i]) == True and check(c[i+1]) == True:
        kq = i
        break
if kq == -1:
    kq = "NOT FOUND"
print(kq)
