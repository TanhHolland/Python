x = int(input())
def check(s) :
    increase = False
    decrease = False
    i = 1
    n = len(s)
    while i < n and s[i-1] < s[i]:
        i+=1
        increase = True
    while i < n and s[i-1] > s[i]:
        i+=1
        decrease = True
    if(i >= n and increase and decrease): return "YES"
    return "NO"
while x > 0:
    x-=1 
    s = input()
    print(check(s))