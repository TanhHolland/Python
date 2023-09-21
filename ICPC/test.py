with open('ICPC/A.txt') as file :
    s = file.read()
ds = s.split()
dict = {}
reg = ".,?"
for i in range(len(ds)) :
    if ds[i][-1] in reg :
        ds[i] = ds[i][:-1]
print(ds)
for i in ds :
    if i not in dict.keys() :
        dict[i] = 1
    else :
        dict[i] +=1
for i in dict.keys() :
    print(i,dict[i])
