x = input()
x = int(x)
while x > 0:
    x -= 1
    a,b,c= input().split()
    a = float(a)
    b = float(b)
    b = b/100
    c = float(c)
    i = 1
    while(a < c):
        a = a + a*b
        i+=1
    print(i-1)