with open('DATA1.in') as file:
   s1 = file.read()
with open('DATA2.in') as file:
   s2 = file.read()
ds1 = s1.lower().split()
ds2 = s2.lower().split()
kq1 = list((set(ds1) - set(ds2)))
kq2 = list((set(ds2) - set(ds1)))
kq1.sort()
kq2.sort()
for i in kq1 :
   print(i,end=" ")
print()
for i in kq2 :
   print(i,end=" ")
