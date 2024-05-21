x = int(input())
while x > 0:
   x-=1
   n = int(input())
   s = [0]
   s += list(map(int,input().split()))
   MAX = int(1e9+5)
   a = [0]*(n+2)
   b = [0]*(n+2)
   b[n+1] = MAX
   for i in range(1,n+1) :
      a[i] = max(s[i],a[i-1])
   for i in range(n,0,-1) :
      b[i] = min(s[i],b[i+1])
   dem = 0
   for i in range(1,n+1) :
      if a[i-1] <= s[i] and s[i] < b[i+1] :
         dem+=1
   print(dem)