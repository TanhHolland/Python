import math
x = int(input())
ds = []
while x > 0:
   x-=1
   s = input()
   ds.append(s)
MIN = 10000
for i in range(len(ds)) :
   dem = 0
   for j in range(len(ds)) :
      if i != j :
         s = ds[j]
         siz = 0
         while siz < len(s) :
            s += s[0]
            s = s[1:]
            siz+=1
            if (s == ds[i]) :
               dem += siz
   MIN = min(dem,MIN)
print(dem)
