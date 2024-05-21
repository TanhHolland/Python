MAX = 10005
a = [0]*MAX
a[0] = a[1] = 1
for i in range(2,MAX//2+1):
    if a[i] == 0 :
        for j in range(i*2,MAX,i) :
            if a[j] == 0 :
                a[j] = 1
                  
n = int(input())
k = []
while len(k) < n:
    k += list(map(int, input().split()))
b = []
for i in k :
    count = 0
    if a[i] != 0 :
        num1 = i
        num2 = i
        while a[num1] != 0 and a[num2] != 0:
            num1 +=1
            num2 -=1
            count +=1
    b.append(count)
print(max(b))