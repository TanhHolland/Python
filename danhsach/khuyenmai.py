n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ds = []
for i in range(len(a)) :
    ds.append((a[i],b[i],a[i]-b[i]))
ds = sorted(ds,key = lambda x : (x[2]))
sum = 0
dem = 0
for i in range(len(ds)) :
    if dem < k :
        dem += 1
        sum += ds[i][0]
    else :
        sum += min(ds[i][0],ds[i][1])
print(sum)