with open('CONTACT.in','r') as file:
   lst = file.readlines()
for i in range(0,len(lst)-1) :
   x = lst[i]
   lst[i] = x[:-1]
chuoi= [i.lower() for i in lst]
kq = []
for i in chuoi :
   if i not in kq :
      kq.append(i)
kq.sort()
for i in kq :
      print(i)