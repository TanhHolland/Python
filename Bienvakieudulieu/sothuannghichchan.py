x = input()
x = int(x)
def check(s) :
    if s != s[::-1] : return False
    for i in s :
        if i not in '02468': return False
    return True
while x > 0:
    x-=1
    n = input()
    for i in range(22,int(n),2):
        if (check(str(i)) and len(str(i)) %2==0 ): print(i,end=" ")
    print()
    