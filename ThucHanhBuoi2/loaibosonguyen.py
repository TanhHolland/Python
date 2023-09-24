with open('DATA.in') as file :
    # ThucHanhBuoi2/
    s = file.read()
kq = []
s = s.split()
for i in s :
    if i.isalpha() == True :
        kq.append(i)
    else :
        if len(i) > 18 :
            kq.append(i)
kq.sort()
for i in kq :
    print(i,end=" ")