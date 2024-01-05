x = int(input())
ds = []
def Try(n,sum,pos,s : str) :
    if sum > n : return
    if sum == n :
        s = s.strip()
        ds.append(s)
        return
    for i in range(pos,0,-1):
        Try(n,sum + i,i,s + str(i)+ ' ')
while x > 0:
    x-=1
    n = int(input())
    Try(n,0,n,'')
    print(len(ds))
    for i in ds :
        print("({}) ".format(i),end="")
    print()
    ds.clear()