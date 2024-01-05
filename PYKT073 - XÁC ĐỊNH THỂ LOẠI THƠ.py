t = int(input()) 
loai = 0
socau = 0
a = []
for _ in range(t) :
    s = input().split()
    if loai == 0 :
        if len(s) == 6 :
            loai = 1
            a.append(loai)
        if len(s) == 7 :
            loai = 2
            socau = 1
        continue
    if loai == 1 :
        if len(s) == 7 :
            loai = 2
            socau = 1
            continue
    if loai == 2 :
        if len(s) == 7 :
            socau +=1
            if socau == 4 :
                socau = 0
                a.append(loai)
        if len(s) == 6 :
            loai = 1
            a.append(loai)
print(len(a))
for i in a :
    print(i)