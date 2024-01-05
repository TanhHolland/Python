import math
x = int(input())

while x > 0:
    x -= 1
    s = input()
    sum1 = 1
    sum2 = 0
    c = False
    for i in range(0, len(s)):
        if i % 2 != 0:
            num = int(s[i])
            sum2 += num
        else:
            if (s[i] != '0'):
                so = int(s[i])
                sum1 *= so
                c = True
    if (c == False):
        sum1 = 0
    print("{} {}".format(sum1, sum2))
