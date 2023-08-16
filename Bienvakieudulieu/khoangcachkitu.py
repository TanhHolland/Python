x = int(input())
def check(s):
    sd = s[::-1]
    for i in range(1,len(s)):
        a = ord(s[i])
        b = ord(s[i-1])
        c = ord(sd[i])
        d = ord(sd[i-1])
        if abs(a - b) != abs(c - d) : return "NO"
    return "YES"
while x > 0 :
    x-=1
    s = input()
    print(check(s))
    
