x = int(input())
def Sotien(s):
   if s[1] == "Xe_con":
      if s[2] == "5" :
         return 10000
      if s[2] == "7" :
         return 15000
   if s[1] == "Xe_tai":
      if s[2] == "2" :
         return 20000
   if s[1] == "Xe_khach":
      if s[2] == "29" :
         return 50000
      if s[2] == "45" :
         return 70000
dict = {}
kq = []
while x > 0:
   x-=1
   s = input().split()
   if s[-2] == "IN" :
      if s[-1] not in dict.keys() :
         dict[s[-1]] = 0
         kq.append(s[-1])
      dict[s[-1]] += Sotien(s)
for i in kq :
   print("{}: {}".format(i,dict[i]))
