t = int(input())
while t > 0:
   t-=1
   n = int(input())
   x,y,z = list(map(int,input().split()))
   a = [0]*(n+1)
   a[1] = x
   for i in range(2,n+1) :
        a[i] = a[i-1] + x
        if i % 2 == 0 :
            a[i] = min(a[i], a[i//2] + z)
        else :
            a[i] = min(a[i],a[(i+1)//2] + z + y)
   print(a[n])
# TEST :3 1 3
#     0 1 2 3 4 5 6
#     0 3 6 9 9 12
#               12