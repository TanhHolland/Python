def result(n : int) :
    return n*(n-1)//2

t = int(input())
a = []
for _ in range(t) :
    a.append(list(input()))
dem = 0
for i in range(t) :
    demc = 0
    demh = 0
    for j in range(t) :
        if a[i][j] == 'C' :
            demh += 1
        if a[j][i] == 'C' :
            demc += 1
    dem += result(demc) + result(demh)
print(dem)