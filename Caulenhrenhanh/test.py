t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    i = 1
    cnt = 0
    while i * (i+1) < 2 * n:
        res = (n*1.0 - i*(i+1)/2)/(i+1)
        if res == int(res):
            print(res, i)
            cnt += 1
        i += 1
    print(cnt)
