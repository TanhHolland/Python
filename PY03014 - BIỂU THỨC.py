t = int(input())
while t > 0:
    t -= 1
    s = input()
    a = []
    b = []
    d = 1
    for i in s:
        if i != '(' and i != ')':
            continue
        if i == '(':
            a.append(d)
            b.append(d)
            d += 1
        else:
            b.append(a[-1])
            a.pop()
    for i in b:
        print(i, end=" ")
    print()
