c = True
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
p = list(p)
while c == True :
    t = input()
    if( t == '0') : break
    k,s = t.split()
    k = int(k)
    s = str(s)
    nhamdan = {}
    for i in range(0,len(p)) :
        nhamdan[p[i]] = i 
    kq = ""
    for i in s:
        kq+= p[(nhamdan[i] + k) % 28]
    print(kq[::-1])
    
    
    