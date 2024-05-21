x = int(input())
def Try(n,k) :
    if k == 1 : return 'A'
    if k == 2**(n-1): return chr(ord('A')+n-1)
    elif k > 2**(n-1) : return Try(n-1,k-2**(n-1))
    else : return Try(n-1,k)
while x > 0:
    x-=1
    n,k = list(map(int,input().split()))
    print(Try(n,k))