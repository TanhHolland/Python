x = input()
x = int(x)
while x > 0:
    x -= 1
    n,k = input().split()
    n,k = int(n),int(k)
    s = list(map(int,input().split()))
    for i in range(k,n):
        print(s[i],end=" ")
    for i in range(0,k):
        print(s[i],end=" ")  
    print()