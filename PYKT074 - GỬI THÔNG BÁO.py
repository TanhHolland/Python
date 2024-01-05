n = int(input())
while n > 0:
    n-=1
    s = input()
    if len(s) < 100 :
        print(s)
    else :
        s = s[:100]
        while s[-1] != ' ' :
            s = s[:-1]
        print(s)