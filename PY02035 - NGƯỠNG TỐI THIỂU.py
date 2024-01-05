s = input()
k = int(input())
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
a.sort()
check = False
for i in a :
    if dict[i] >= k :
        check = True
        print(i,dict[i])
if check == False :
    print("NOT FOUND")