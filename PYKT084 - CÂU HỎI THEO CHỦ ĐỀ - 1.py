n = int(input())
kq = []
d = {}
dem = 0
loai = ""
for i in range(n) :
    s = input()
    if i == 0 :
        kq.append(s)
        loai = s
        d[s] = 0
    elif s == "" :
        loai = ""
    else :
        if loai != "" :
            d[loai] += 1
        else :
            loai = s
            kq.append(loai)
            d[loai] = 0
    # n,k = list(map(int,input().split()))
    # s = list(map(int,input().split()))
for i in kq :
    print("{}: {}".format(i,d[i]))
