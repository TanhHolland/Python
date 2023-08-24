x = int(input())
MAX = 1000005
a = [0]*MAX
a[0] = 1
a[1] = 1
for i in range(2,MAX//2 + 1) :
    if a[i] == 0 :
        for j in range(i*2,MAX,i):
            if a[j] == 0 :
                a[j] = 1
while x > 0:
    x -= 1
    n = int(input())
    c = 0
    for i in range(2,n-6) :
        if (a[i] == 0 and a[i+2]== 0 and a[i+6] == 0) or (a[i]==0 and a[i+4] ==0 and a[i+6]==0) : c+=1
    print(c)
        