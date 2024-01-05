t = int(input())
a = []
while t > 0 :
    t-=1
    s = input()
    n,m = list(map(int,input().split()))
    a.append((s,n,m))
a = sorted(a,key=lambda x : (-x[1],x[2],x[0]))
for i in a :
    print(i[0],i[1],i[2])