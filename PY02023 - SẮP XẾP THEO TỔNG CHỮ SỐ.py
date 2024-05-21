x = int(input())
def check(item) :
    sum = 0
    n = item
    while (n > 0) :
        sum += n%10
        n//=10
    return(sum,item)
while x > 0:
    x-=1
    n = input()
    s = list(map(int,input().split()))
    a = sorted(s,key=check)
    for i in a :
        print(i,end=" ")
    print()