n,k = input().split()
n,k = int(n),int(k)
s = [int(x) for x in input().split()]
ds = []
for i in s:
    if i not in ds :
        ds.append(i)
ds.sort()
a = []
def Try(pos,dem) :
    if dem == k :
        for i in a :
            print(i,end=" ")
        print()
        return
    for i in range(pos,len(ds)) :
        a.append(ds[i])
        Try(i+1,dem+1)
        a.pop()
Try(0,0)