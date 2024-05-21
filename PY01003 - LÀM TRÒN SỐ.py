for t in range(int(input())) :
    n = input()
    s = n[0] + '4'*(len(n)-1)
    s2 = n[0] + '0'*(len(n)-1)
    s3 = str(int(n[0])+1) + '0'*(len(n)-1)
    ok = 1
    for i in range(len(n)) :
        if int(n[i])>int(s[i]) :
            print(s3)
            ok=0
            break
        elif int(n[i])<int(s[i]):
            print(s2)
            ok=0
            break
    if ok==1 :
        print(s2)