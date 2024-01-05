# n,k = input().split()
# n,k = int(n),int(k)
# s = [int(x) for x in input().split()]
# ds = []
# for i in s:
#     if i not in ds :
#         ds.append(i)
# ds.sort()

for t in range(int(input())) :
    n,p = [int(x) for x in input().split()]
    d = 0
    for i in range(2,n+1) :
        while i %p == 0 :
            i /=p
            d+=1
    print(d)