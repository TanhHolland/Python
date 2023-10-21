n = int(input())
a = list(map(int,input().split()))
res = 100000
for i in range(1,n-1) :
   b = [0]*n
   b[i] = a[i]
   dem = 0
   for j in range(i-1,-1,-1) :
      if a[j] >= b[j+1] :
         dem += a[j] - b[j+1] + 1
      else :
         dem += b[j+1] - a[j] - 1
      b[j] = b[j+1] - 1
   for j in range(i+1,n,1) :
      if a[j] >= b[j-1] :
         dem += a[j] - b[j-1] + 1
      else :
         dem += b[j-1] - a[j] - 1
      b[j] = b[j-1] - 1
   if b.count(0) > 0 :
      continue
   res = min(dem,res)
print(res)