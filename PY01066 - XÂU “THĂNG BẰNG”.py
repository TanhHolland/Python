n = int(input())
def check(s1) :
    s2 = s1[::-1]
    for i in range(len(s1)-1) :
        a = ord(s1[i])
        b = ord(s1[i+1])
        c = ord(s2[i])
        d = ord(s2[i+1])
        if abs(a-b) != abs(c-d) : return 'NO'
    return 'YES'
for _ in range(n) :
    s = input()
    print(check(s))