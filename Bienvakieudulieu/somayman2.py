n = int(input())
while n > 0:
    n-=1
    x = input()
    c = True
    for i in x:
        if(i != '4' and i !='7'):
            c = False
            break
    if(c): print("YES")
    else: print("NO")