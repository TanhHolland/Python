x = input()
x = int(x)
def check(s) :
    for i in s:
        if(i != '0' and i != '1' and i != '2'): return "NO"
    return "YES"
while x > 0:
    x-=1
    s = input()
    print(check(s))
