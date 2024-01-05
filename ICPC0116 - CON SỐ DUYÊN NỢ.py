x = int(input())
while x > 0:
    x-=1
    s = input()
    if s[0] == s[len(s)-1] : print("YES")
    else: print("NO")