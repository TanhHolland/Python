x = int(input())
while x > 0:
    x-=1
    s = input()
    xau = s
    s = s.replace("and","")
    s = s.replace("of","")
    s = s.replace("in","")
    ds = s.split()
    for i in range(0,len(ds)):
        print(ds[i][0],end="")
    print(" " + xau)