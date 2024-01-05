x = input()
x = int(x)
def ucln(a,b) :
    if b == 0 : return a
    return ucln(b,a%b)
while x > 0:
    x -= 1
    s1 = int(input())
    s2 = int(input())
    print(ucln(s1,s2))

