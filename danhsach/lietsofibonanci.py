x = int(input())
a = [1,1]
for i in range(2,94) :
    a.append(a[i-1] + a[i-2])
while x > 0 :
    x-=1
    c,d = input().split()
    c = int(c)
    d = int(d)
    for i in range(c,d+1):
        print(a[i-1],end=" ")
    print()
    