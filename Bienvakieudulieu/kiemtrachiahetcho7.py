x = int(input())
def convert(n) :
    sum = 0
    while n > 0 :
        sum = sum*10 + n%10
        n//=10
    return sum
while x > 0:
    x -= 1
    dem = 1000
    n = int(input())
    while dem > 0:
        dem-=1
        if(n % 7 == 0) :
            print(n)
            break
        n = n + convert(n)
    if(dem <= 0): print("-1")    