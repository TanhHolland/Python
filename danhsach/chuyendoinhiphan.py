with open('DATA.in') as file :
    ob = file.read()
ob = ob.split()
x = int(ob[0])
d = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def convert(n,coso) :
    result = ''
    while n > 0 :
        result += d[n%coso]
        n //= coso
    return result[::-1]
i = 1
while x > 0:
    x-=1
    coso = int(ob[i])
    s = ob[i+1]
    n = int(s,2)
    print(convert(n,coso))
    i+=2
    