x = int(input())
MAX = 10000005
a = [0]*MAX
a[0] = 1
a[1] = 1
for i in range(2, MAX//2 + 1):
    if a[i] == 0:
        for j in range(2, MAX, i):
            if a[j] == 0:
                a[j] = 1


def check(n):
    if a[n] == 1:
        return "No"
    m = 0
    sum = 0
    while n > 0:
        temp = n % 10
        sum+=temp
        if a[temp] == 1:
            return "No"
        m = m * 10 + temp
        n //= 10
    if a[sum] == 1 or a[m] == 1: return "No"
    return "Yes"

while x > 0:
    x -= 1
    n = int(input())
    print(check(n))
