x = int(input())
dict = {}
kq = []
ok = 0
for i in range(1,x+1) :
   s = input()
   if i == 1 :
      dict[s] = 0
      kq.append(s)
   elif s == "":
      ok = 1
   else :
      if ok == 1:
         dict[s] = 0
         kq.append(s)
         ok = 0
      else :
         dict[kq[-1]] +=1
for i in kq :
   print("{}: {}".format(i,dict[i]))
      
   
