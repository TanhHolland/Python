import sys
ds = []
for line in sys.stdin :
   ds += list(map(int,line.split()))
x = ds[0]
i = 1
for _ in range(x):
   n,c,d = ds[i],ds[i+1],ds[i+2]
   i+=3
   a = []
   for j in range(n):
      a.append(ds[i+j])
   i+=n
   a = sorted(a,reverse=True)
   id = 0
   dmax = []
   dmin = []
   for _ in range(min(c,d)) :
      dmax.append(a[id])
      id+=1
   for _ in range(max(c,d)) :
      dmin.append(a[id])
      id+=1
   s = sum(dmax)/len(dmax) + sum(dmin)/len(dmin)
   print("{:.6f}".format(s))
   