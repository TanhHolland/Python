def giao (a,b) :
    a.sort()
    b.sort()
    if len(set(a)) != len(set(b)) :
        return "NO"
    kq = set(a) & set(b)
    if set(a) != kq :
        return "NO"
    return "YES"
n = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
a = giao(s1,s2)
print(a)