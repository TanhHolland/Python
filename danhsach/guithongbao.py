x = int(input())
while x > 0:
   x-=1
   s = list(input())
   if len(s) <= 100 :
      print(''.join(s))
   else :
      s = s[:100]
      while s[-1] != " " :
         del s[-1]
      print(''.join(s))