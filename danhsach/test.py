n = int(input())
a = []
while len(a) < n:
    a += list(map(int, input().split()))
while True :
    s = 0
    b = []*n
    for j in range(len(a)):
        b[j] = a[j]//i
    print(b)
    print(s)
