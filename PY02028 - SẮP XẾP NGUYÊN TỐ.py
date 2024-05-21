MAX = 1005
a = [0]*MAX
a[0] = a[1] = 1
for i in range(2,MAX//2 + 1) :
    if a[i] == 0:
        for j in range(i*2,MAX,i):
            if a[j] == 0:
                a[j] = 1
n = int(input())
s = []
while len(s) < n:   
    s = list(map(int, input().split()))
b = []
for i in s :
    if a[i] == 0:
        b.append(i)
b.sort()
i = 0
for j in s :
    if a[j] == 0 :
        j = b[i]
        i+=1
    print(j,end=" ")