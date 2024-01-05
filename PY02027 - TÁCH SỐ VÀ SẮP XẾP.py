import re
x = int(input())
kq = []
while x > 0:
   x -= 1
   s = input()
   ds = re.findall(r'\d+',s)
   ds = map(int,ds)
   kq += ds
kq.sort()
for i in kq :
   print(i)