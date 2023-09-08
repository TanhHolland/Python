n = int(input())
loai = 0
socau = 0
a = []
while n > 0:
    n -= 1
    s = input().split()
    if loai == 0:
        if len(s) == 6 :
            loai = 1
            a.append(loai)
        if len(s) == 7:
            loai = 2
            socau = 1
        continue
    if loai == 1:
        socau = 0
        if len(s) == 6 or len(s) == 8:
            continue
        if len(s) == 7:
            loai = 2
            socau = 1
            continue
    if loai == 2:
        if len(s) == 7 :
            socau +=1
            if socau == 4 :
                a.append(loai)
                socau = 0
            continue
        if len(s) == 6 :
            loai = 1
            a.append(loai)
print(len(a))
for i in a:
    print(i)
