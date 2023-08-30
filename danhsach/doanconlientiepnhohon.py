x = int(input())
while x > 0:
    x-=1
    n = int(input())
    s = list(map(int,input().split()))
    a = [1]*n
    for i in range(1,n) :
        j = i - 1
        while j >=0 and s[i] >= s[j] :
            a[i] += a[j]
            j -= a[j]
    for i in a :
        print(i,end=" ")
    print()