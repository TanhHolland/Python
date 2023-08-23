x = int(input())
MAX = 2000005
a = [0] * MAX
a[0] = 1
a[1] = 1
for i in range(2, MAX//2 + 1):
    if (a[i] == 0):
        for j in range(i*2, MAX, i):
            if a[j] == 0:
                a[j] = i
for i in range(2, MAX):
    if a[i] == 0:
        a[i] = i
sum = 0
while x > 0:
    x -= 1
    n = int(input())
    while n > 1:
        sum += a[n]
        n //= a[n]
print(sum)
