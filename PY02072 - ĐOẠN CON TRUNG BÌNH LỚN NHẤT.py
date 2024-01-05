# n,k = list(map(int,input().split()))
t = int(input())
s = list(map(int,input().split()))
s.append(-99)
maxx = max(s)
lht = 0
lmax = 0
for i in range(len(s)) :
    if s[i] == maxx :
        lht +=1
    else :
        lmax = max(lmax,lht)
        lht = 0
print(lmax)