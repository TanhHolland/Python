x = int(input())
def check(n):
    if len(n) %2 == 0: return "NO"
    if(n[0] == n[1]): return "NO"
    for i in range(2,len(n),2):
        if (n[i] != n[i-2]): return "NO"
    return "YES"
while x > 0:
    x-=1
    n = input()
    print(check(n))
    