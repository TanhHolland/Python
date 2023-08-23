x = int(input())
a = [1,1]
for i in range(2,93) :
    a.append(a[i-1] + a[i-2])
while x > 0 :
    x-=1
    a,b = list(map(int,input().split()))
    