def check (a,b) :
    if len(a) != len(b) :
        return 'NO'
    a,b = list(a),list(b)
    for i in range(len(a)) :
        if a[i] != b[i] :
            return 'NO'
    return 'YES'
n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = set(a)
b = set(b)
print(check(a,b))
    