ds = []
def Try(s : str,n,a,b,c,d) :
    if len(s) == n and a > 0 and b > 0 and c > 0 and d > 0 and int(s[-1]) % 2 == 1:
        global ds
        ds.append(int(s))
    if len(s) < n :
        Try(s + '2',n,a+1,b,c,d)
        Try(s + '3',n,a,b+1,c,d)
        Try(s + '5',n,a,b,c+1,d)
        Try(s + '7',n,a,b,c,d+1)
n = int(input())
for i in range(4,n+1):
    Try('',i,0,0,0,0)
for i in ds :
    print(i)