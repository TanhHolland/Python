x = input()
x = int(x)
while x > 0:
    x -= 1
    a = float(input())
    b = float(input())
    c = float(input())
    i = 0
    while(c < a):
        c = c*((1 + b/100)**i)
        i+=1
    print(i)