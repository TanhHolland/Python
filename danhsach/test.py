n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ds = []
for i in range(n) :
   ds.append((a[i],b[i]))
ds = sorted(ds,key=lambda x : (x[1],x[0]))
cnt = 0
sum = 0
for i in range(n) :
   if cnt < k :
      x = ds[i]
      
