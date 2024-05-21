import re
x = input()
x = int(x)
while x > 0:
    x -= 1
    s = input()
    ds = re.findall(r'\d+', s)
    ds = map(int, ds)
    print(max(ds))
