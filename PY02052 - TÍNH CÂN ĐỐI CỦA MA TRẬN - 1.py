x = int(input())
a = []
while x > 0:
    x-=1
    s = list(map(int,input().split()))
    a.append(s)
k = int(input())
sum1 = 0
sum2 = 0
for i in range(0,len(a)) :
    for j in range(i+1,len(a[i])):
        sum1+=a[i][j]
        sum2+=a[j][i]
sum = abs(sum1 - sum2)
if(sum <= k): print("YES")
else: print("NO")
print(sum)
    
    