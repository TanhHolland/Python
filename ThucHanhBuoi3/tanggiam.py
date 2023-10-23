t = int(input())
for _ in range(t) :
    n = int(input())
    a,b = [],[]
    for _ in range(n) :
        res = list(map(float,input().split()))
        a.append(res[0])
        b.append(res[1])
    dp = [0] * 501
    ans = -10 **18
    for i in range(n) :
        dp[i] = 1
        for j in range(i) :
            if a[i] > a[j] and b[i] < b[j] : dp[i] = max(dp[i],dp[j] + 1)
        ans = max (ans,dp[i])
    print(ans)