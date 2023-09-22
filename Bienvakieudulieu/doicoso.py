x = int(input())
d = ['0','1','2','3','4','5','6','7','8','9']
for i in range(0,26) :
    d.append(chr(ord('A') + i))
while x > 0:
    x-=1
    a,b = list(map(int,input().split()))
    result = ''
    while a > 0:
        result += d[a%b]
        a//=b
    print(result[::-1])
    