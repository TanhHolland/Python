x = int(input())
s = list(map(int,input().split()))
mid = x//2
res = 1000000
MIN = 1000000
for j in range(0,len(s)) :
    count = 0
    for i in range(0,len(s)) :
        if i != j :
            count += abs(s[i] - s[j])
    if count < MIN :
        MIN = count
        res = s[j]
print("{} {}".format(MIN,res))