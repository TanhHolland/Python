x = int(input())
MAX = 1000005
a = [0]*MAX
a[0] = 1
a[1] = 1
for i in range(2, MAX//2 + 1):
    if a[i] == 0:
        for j in range(i*2, MAX, i):
            if a[j] == 0:
                a[j] = 1
snt = []
for i in range(2, MAX):
    if (a[i] == 0):
        snt.append(i)
while x > 0:
    x -= 1
    n = int(input())
    for i in snt:
        a[i] = 0
    for i in range(13, n+1):
        if a[i] == 0:
            lst = list(str(i))
            lst.reverse()
            so = "".join(lst)
            so = int(so)
            if so != i and so <=n and a[so] == 0:
                print("{} {} ".format(i, so),end = "")
                a[so] = 1
    print()
