x = input()
x = int(x)
while x > 0:
    x -= 1
    a,b,c= input().split()
    c = float(c)
    b = float(b)
    a = float(a)
    i = 0
    while(c < a):
        c = c*((1 + b/100)**i)
        i+=1
    print(i)