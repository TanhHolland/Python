t = int(input())
while t > 0:
    s = input()
    t -= 1
    sum = 0
    check = True
    for i in range(1, len(s)):
        x = int(s[i])
        y = int(s[i-1])
        if abs(x - y) != 2:
            check = False
            break
    for i in s:
        k = int(i)
        sum += k
    if (check == True and sum % 10 == 0):
        print("YES")
    else:
        print("NO")
