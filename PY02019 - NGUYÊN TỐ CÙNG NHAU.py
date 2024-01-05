x = int(input())
s = list(map(int,input().split()))
s.sort()
def gcd(a,b) :
    if b == 0 : return a
    return gcd(b,a%b)
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if gcd(s[i],s[j]) == 1 :
            print(s[i],s[j])

    