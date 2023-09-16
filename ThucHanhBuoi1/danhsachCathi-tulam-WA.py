with open('ThucHanh1/CATHI.in','r') as file :
    s = file.readlines()
def suaNgaythi(ngaythi) :
    lst = ngaythi.split('/')
    for i in range(0,len(lst)-1) :
        if len(lst[i]) < 2 :
            lst[i] = '0' + lst[i]
    s = ""
    for i in range(0,len(lst)-1) :
        s += lst[i]+'/'
    s+=lst[-1]
    return s
def suaTime(time) :
    lst = time.split(':')
    for i in range(0,len(lst)) :
        if len(lst[i]) < 2 :
            lst[i] = '0' + lst[i]
    s = ""
    for i in range(0,len(lst)-1) :
        s += lst[i]+':'
    s+=lst[-1]
    return 
n = int (s[0])
del s[0]
for i in range(0,len(s)-1) :
    s[i] = s[i][:-1]
print(s)
ds = []
dem = 1
while n > 0:
    n-=1
    macathi = str(dem)
    while len(macathi) <3 :
        macathi = '0' + macathi 
    macathi = 'C'+ macathi
    ngaythi = s[0]
    del s[0]
    time = s[0]
    del s[0]
    id = s[0]
    del s[0]
    ngaythi = suaNgaythi(ngaythi)
    time = suaTime(time)
    tup = (macathi,ngaythi,time,id)
    ds.append(tup)
    dem+=1
ds = sorted(ds,key= lambda item : (item[1],item[2],item[0]))
for i in ds :
    print(i[0],i[1],i[2],i[3])

    