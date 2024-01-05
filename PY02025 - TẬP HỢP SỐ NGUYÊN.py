def giao (a,b) :
    return list(set(a) & set(b))
def hieu(a,b) :
    return list(set(a) - set(b))
n = list(map(int, input().split()))
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
a = giao(s1,s2)
b = hieu(s1,s2)
c = hieu(s2,s1)
a.sort()
b.sort()
c.sort()
for i in a :
    print(i,end=" ")
print()
for i in b :
    print(i,end=" ")
print()
for i in c :
    print(i,end=" ")
