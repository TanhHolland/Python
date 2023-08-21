x = int(input())
def hehe(n,a,b,c) :
    if n == 1 :
        print("{} -> {}".format(a,c))
        return
    hehe(n-1,a,c,b)
    hehe(1,a,b,c)
    hehe(n-1,b,a,c)
hehe(x,"A","B","C")