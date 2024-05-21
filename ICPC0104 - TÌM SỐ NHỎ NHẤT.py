import re
x = int(input())
while x > 0:
    x-=1
    s = input()
    ds = re.findall(r'\d+',s)
    ds = map(int,ds)
    print(min(ds))