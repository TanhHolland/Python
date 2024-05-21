x = int(input())
while x > 0:
    x-=1
    s = input()
    k = s[len(s)-2:]
    if k == "86": print("YES")
    else: print("NO")