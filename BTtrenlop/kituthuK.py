t = int(input())
def check(n : int, k : int) :
    if n == 1 : return 'A'
    if k == 2**(n-1) : return chr(ord('A') + n -1)
    if k > 2**(n-1) : return check(n-1, k - 2**(n-1))
    if k < 2**(n-1) : return check(n-1,k)
while t > 0 :
    t-=1
    a,b = list(map(int,input().split()))
    print(check(a,b))