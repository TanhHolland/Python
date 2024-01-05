x = int(input())
s = list(map(int,input().split()))
MAX = int(1e6)
a = [0]*MAX
a[0] = a[1] = 1
for i in range(2,MAX//2 + 1) :
    if a[i] == 0:
        for j in range(i*2,MAX,i) :
            if a[j] == 0:
                a[j] = 1
b = []
for i in s :
    if a[i] == 0 and i not in b:
        print(i,s.count(i))
        b.append(i)
