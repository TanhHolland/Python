n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lst = []
for i in range(n) :
    lst.append([a[i],b[i],a[i]-b[i]])
lst = sorted(lst,key= lambda x : (x[2]))
sum = 0
for i in range(n) :
    if i < k :
        sum += lst[i][0]
    else :
        sum += min(lst[i][0],lst[i][1])
print(sum)