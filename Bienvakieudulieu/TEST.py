n = int(input())
a = [0]*(n+1)
a[0] = 1
a[1] = 1
for i in range(2, n//2+1):
    if a[i] == 0:
        for j in range(i*2, n+1, i):
            if a[j] == 0:
                a[j] = i
for i in range(2, n+1):
    if a[i] == 0:
        a[i] = i
ds = []
result = 0
for i in range(2, n+1):
    x = i
    count = 0
    while i > 1:
        count += 1
        i = i//a[i]
    count += 1
    if count == 9:
        result += 1
        ds.append(x)
print(len(ds))
