import re
x = int(input())
while x > 0:
    x-=1
    s = input()
    so = list(map(int,re.findall(r'\d',s)))
    kitu = re.findall(r'[a-zA-Z]',s)
    kitu.sort()
    print(''.join(kitu) + str(sum(so)))
    