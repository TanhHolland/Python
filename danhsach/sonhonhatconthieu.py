x = int(input())
s = list(map(int,input().split()))
l = min(s)
r = max(s)
i = l+1
while i <= r :
    if i not in s :
        break
    else : i +=1
print(i)