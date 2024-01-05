# n,k = input().split()
# n,k = int(n),int(k)
# s = [int(x) for x in input().split()]
# ds = []
# for i in s:
#     if i not in ds :
#         ds.append(i)
# ds.sort()
a = []
s = input()
c = [0] * 12


def Try():
    if len(a) == len(s):
        for i in a:
            print(i, end='')
        print()
        return
    for i in range(len(s)):
        if c[i] == 0:
            c[i] = 1
            a.append(s[i])
            Try()
            a.pop()
            c[i] = 0


Try()
