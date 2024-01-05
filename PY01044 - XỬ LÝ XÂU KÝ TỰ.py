s1 = input().lower().split()
s2 = input().lower().split()
kq1 = list(set(s1) | set(s2))
kq2 = list(set(s1) & set(s2))
kq1.sort()
kq2.sort()
for i in kq1:
    print(i, end=" ")
print()
for i in kq2:
    print(i, end=" ")
