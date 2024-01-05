def check(s) :
    i = 0
    k = s[i]
    j = 1
    t = s[j]
    n = len(s)
    while i < n :
        if s[i] != k: return False
        i += 2
    while j < n :
        if s[j] != t: return False
        j += 2
    if(k == t ): return False
    return True
x = int (input())
while x > 0 :
    x-=1
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")