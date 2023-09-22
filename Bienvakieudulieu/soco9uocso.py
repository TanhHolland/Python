MAX = int(1e9+5)
a = [0]*(int(1e9+5))
a[0] = 1
a[1] = 1
for i in range(2, MAX//2+1):
    if a[i] == 0:
        a[i] += 2
    for j in range(i*2, MAX+1, i):
        if a[j] == 0 :
            a[j] +=2
        a[j] += 1
for i in range(2, MAX+1):
    if a[i] == 0:
        a[i] = 2
n = int(input())
dem = 0
for i in range(2, n+1):
    if a[i] == 9 : dem+=1
print(dem)
