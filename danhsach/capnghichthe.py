x = int(input())
s = list(map(int,input().split()))
c = 0
for i in range(0,len(s)-1) :
    for j in range(i+1,len(s)):
        if s[i] > s[j] : c+=1
print(c)