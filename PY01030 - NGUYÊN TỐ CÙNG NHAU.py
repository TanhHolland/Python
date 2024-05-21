n,k = input().split()
n = int(n)
k = int(k)
def gcd(a,b):
    if b == 0 : return a
    return gcd(b,a%b)
count = 0
for i in range(10**(k-1),10**(k)) :
    if gcd(n,i) == 1:
        count += 1
        print(i,end=" ")
    if count == 10 :
        print()
        count = 0