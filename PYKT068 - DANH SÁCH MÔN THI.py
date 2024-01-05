t = int(input())
a = []
while t > 0:
    t-=1
    a.append((input(),input(),input()))
a  = sorted(a,key= lambda x :(x[0]))
for i in a :
    print(i[0],i[1],i[2])