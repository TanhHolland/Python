import math
x = int(input())

while x > 0:
    x -= 1
    s = input()
    sum1 = 0
    sum2 = 1
    c = False
    for i in range(0, len(s)):
        if i % 2 == 0:
            num = int(s[i])
            sum1 += num
        else:
            if (s[i] != '0'):
                so = int(s[i])
                sum2 *= so
                c = True
    if (c == False):
        sum2 = 0
    print("{} {}".format(sum1, sum2))
