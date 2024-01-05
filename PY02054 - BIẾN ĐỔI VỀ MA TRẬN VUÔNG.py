n,m = map(int,input().split())
t = n
s = []
while t > 0:
   t-=1
   xau = list(map(int,input().split()))
   s.append(xau)
if n > m :
   dong = n-m
   dem = 0
   for i in range(0,len(s)) :
      if i % 2 == 0 and dem < dong:
         dem+=1
         continue
      for j in s[i] :
         print(j,end= " ")
      print()
elif n < m :
   cot = m - n
   for i in range(0,len(s)) :
      dem = 0
      for j in range(0,len(s[i])) :
         if j % 2 == 1 and dem < cot:
            dem+=1
            continue
         print(s[i][j],end=" ")
      print()
else :
   for i in range(len(s)) :
      for j in range(len(s[i])) :
         print(s[i][j],end=" ")
      print()
            
   
    