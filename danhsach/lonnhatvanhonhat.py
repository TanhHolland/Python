while True:
    n = int(input())
    if n == 0: break
    a = []
    d = n
    while d > 0:
        d-=1
        x = int(input())
        a.append(x)
    if a.count(a[0]) == n :
        print("BANG NHAU")
    else :
        print("{} {}".format(min(a),max(a)))