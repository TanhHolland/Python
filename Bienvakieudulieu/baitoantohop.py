n,k = input().split()
n,k = int(n),int(k)
s = [int(x) for x in input().split()]
ds = []
for i in s:
    if i not in ds :
        ds.append(i)
ds.sort()
a = []

def Try(i,pos) :
    if len(a) == k :
        for x in a :
            print(x, end= " ")
        print()
        return
    for j in range(pos,len(ds)) :
        a.append(ds[j])
        Try(i+1,j+1)
        a.pop()
Try(0,0)
