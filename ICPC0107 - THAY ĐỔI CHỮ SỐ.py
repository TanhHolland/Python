x = int(input())


def check(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)


while x > 0:
    x -= 1
    p, q = input().split()
    if (int(p) > int(q)):
        p, q = q, p
    s = input().split()
    if(len(s) > 1) :
        a = s[0]
        b = s[1]
    else :
        a = s[0]
        b = input()
    print(check(a, b, q, p), check(a, b, p, q))
