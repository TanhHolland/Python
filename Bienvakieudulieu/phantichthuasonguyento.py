x = input()
x = int(x)
while x > 0:
    x-=1
    n = int(input())
    i = 2
    print("1",end="")
    while n > 1 :
        dem = 0
        while(n%i == 0):
            n = n/i
            dem += 1
        if(dem > 0) :
            print(" * {}^{}".format(i,dem),end="")
        i += 1
    print()