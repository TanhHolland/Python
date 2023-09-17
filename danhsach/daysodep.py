x = int(input())
while x > 0:
   x -= 1
   n = input()
   a = list(map(int, input().split()))
   i = 0
   dem = 0
   while i < len(a) - 1:
      if max(a[i], a[i+1]) > 2* min(a[i], a[i+1]):
         so = (max(a[i], a[i+1]) + 1)//2
         a.insert(i+1, so)
         dem+=1
      else:
         i += 1
   print(dem)
