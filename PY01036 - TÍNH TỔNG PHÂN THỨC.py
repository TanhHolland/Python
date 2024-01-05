x = int(input())
def chan(n):
    sum = 0
    for i in range(2,n+1,2):
        sum += 1/i
    return sum
def le(n):
    sum = 0
    for i in range(1,n+1,2):
        sum += 1/i
    return sum
while x > 0:
    x-=1
    kq = 0
    n = int(input())
    if(n % 2 == 0): kq = chan(n)
    else: kq = le(n)
    kq = "{:.6f}".format(kq)
    print(kq)
    