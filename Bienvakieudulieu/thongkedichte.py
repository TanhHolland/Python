n,m = list(map(int,input().split()))
a = []
c = []
x = [-1,-1,0,1,1,1,0,-1]
y = [0,1,1,1,0,-1,-1,-1]
def check(n,m,i,j) :
    if i < 0 or i >= n : return False
    if j < 0 or j >= m : return False
    return True
for i in range(n) :
    s = list(map(int,input().split()))
    c.append([0]*(len(s)))
    a.append(s)
dem = 0
for i in range(n) :
    for j in range(m) :
        if a[i][j] == -1 :
            for k in range(8) :
                if check(n,m,i + x[k], j + y[k]) == True and c[i + x[k]][j + y[k]] == 0:
                    c[i + x[k]][j + y[k]] = 1
                    dem += a[i + x[k]][j + y[k]]
print(dem)