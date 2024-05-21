s = input()
n = len(s)
if n % 2 == 1 :
    n-=1
a = []
dict = {}
for i in range(0,n,2) :
    so = int(s[i:i+2])
    if so not in a :
        a.append(so)
        dict[so] = 1
    else :
        dict[so] +=1
# a.sort()
for i in a :
    print(i,dict[i])
    