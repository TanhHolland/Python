x = int(input())
kq = []
a = [0]*10
c = [0]*10
def Try(d, n):
    for i in range(1, n+1):
        if c[i] == 0:
            c[i] = 1
            a[d] = i
            if d == n:
                s = ""
                for j in range(1, n+1):
                    s += str(a[j])
                kq.append(s)
            else:
                Try(d+1, n)
            c[i] = 0
while x > 0:
    x -= 1
    n = int(input())
    for i in range(1, n+1):
        a[i] = 1
        c[i] = 0
    kq.clear()
    Try(1,n)
    kq.reverse()
    print(len(kq))
    for i in kq :
        print(i,end=" ")
    print()
