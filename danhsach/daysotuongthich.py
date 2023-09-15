n = int(input())
a = list(map(int,input().split()))
j = 1
while True:
   b = [j]*n
   for i in range(0,n-1) :
      b[i+1] = (b[i] * a[i+1])//a[i]
   k = a[0] // b[0]
   check = True
   for z in range(1,n) :
      if b[z] == 0 : b[z] +=1
      while ( a[z] // b[z] ) > k :
         b[z] += 1
      if ( a[z] // b[z] ) < k and check == True:
         check = False
   if check == True :
      print(sum(b))
      break
   else: j+=1