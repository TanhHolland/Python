with open("DATA.in") as file :
    s = file.read()
s = s.split()
b = []
for i in s :
    if i.isdigit() == False or len(i) > 18 :
        b.append(i)
b.sort()
for i in b :
    print(i,end=" ")