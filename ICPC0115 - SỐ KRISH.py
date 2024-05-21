x = int(input())
ds = [1]
for i in range(1,10) :
        ds.append(ds[-1] * int(i))
while x > 0:
    x-=1
    s = input()
    sum = 0
    for i in s :
        i = int(i)
        sum+=ds[i]
    if str(sum) == s : print("Yes")
    else: print("No")