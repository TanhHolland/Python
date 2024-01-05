dem = 0
c = 0
b = []
while dem < 10:
    s = list(map(int, input().split()))
    b += s
    dem += len(s)
a = []
for i in b:
    temp = i % 42
    if temp not in a:
        a.append(temp)
print(len(a))
