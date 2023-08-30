x = int(input())
n = x
a = []
dem = 0
def tinhKq(n) :
    if n < 2 : return 0
    return (n*(n-1))//2
while x > 0:
    x-=1
    s = list(input())
    a.append(s)
for i in range(0,n) :
    row = 0
    col = 0
    for j in range(0,n) :
        if a[i][j] == 'C': row += 1
        if a[j][i] == 'C': col += 1
    dem += tinhKq(row) + tinhKq(col)
print(dem)
            