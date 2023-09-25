x = int(input())
def ucln(a,b) :
    if b == 0 : return a
    return ucln(b,a%b)
while x > 0:
    x-=1
    s = input()
    sdao = s[::-1]
    print(sdao)
    s = int(s)
    sdao = int(sdao)
    UCLN = ucln(s,sdao)
    BCNN = (s*sdao) // UCLN
    print(UCLN)
    print(BCNN)
    
    