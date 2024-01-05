x = input()
d1 = 0
d2 = 0
for i in x:
    if (i >= 'A' and i <= 'Z'):
        d1 += 1
    else:
        d2 += 1
if (d1 <= d2):
    print(x.lower())
else:
    print(x.upper())
