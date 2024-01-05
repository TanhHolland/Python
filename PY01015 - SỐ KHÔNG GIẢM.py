x = input()
x = int(x)
while x > 0:
    x -= 1
    s = input()
    c = True
    for i in range(1, len(s)):
        if (s[i] < s[i-1]):
            c = False
            break
    if (c):
        print("YES")
    else:
        print("NO")
