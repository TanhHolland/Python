x = int(input())
def check(n):
    sum = 0
    for i in n:
        a = int(i)
        sum += a
    sum = str(sum)
    if(len(sum) < 2) :return "NO"
    sum2 = sum[::-1]
    if(sum2 == sum): return "YES"
    return "NO"
while x > 0:
    x-=1
    n = input()
    print(check(n))
    