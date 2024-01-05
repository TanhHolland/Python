x = int(input())
a = []
while x >0:
    x-=1
    s = input()
    if s not in a : a.append(s)
print(len(a))