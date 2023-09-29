l,h = input().split()
l = int(l)
h = int(h)
p = input()
MAX = int(1e7)
a = [0]*MAX
a[0] = a[1] = 1
for i in range(2,MAX//2+1) :
    if a[i] == 0:
        for j in range(i*2,MAX,i):
            if a[j] == 0:
                a[j] = 1
ds = []
for i in range(2,MAX) :
    if a[i] == 0:
        ds.append(i)
dem = 0
for i in range(l-1,h+1) :
    s = str(ds[i])
    if s.find(p) != -1 :
        dem+=1
print(dem)