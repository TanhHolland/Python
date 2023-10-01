with open("CATHI.in") as file:
    s = file.read().split()
t = int(s[0])
a = []
i = 1
for id in range(t) :
    id = "C" + "{:03d}".format(id+1)
    a.append((id,s[i],s[i+1],s[i+2]))
    i+=3
a = sorted(a,key= lambda x: (x[2],x[0]))
for i in a :
    print(i[0],i[1],i[2],i[3])