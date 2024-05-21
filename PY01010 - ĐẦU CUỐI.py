x = input()
x = int(x)
while x > 0:
    x-=1
    s = input()
    n = len(s)
    a = s[:2]
    b = s[n-2:]
    if(a == b): print("YES")
    else: print("NO")