n = int(input())
def check (s : str) :
    a = list(map(int,list(s)))
    # 4312 4132 4231 345
    i = len(s)-2
    while i >= 0 :
        if a[i] < a[i+1] :
            i-=1
        else : 
            break
    if i < 0 : return '-1'
    #  i = 1
    MAX = -1
    pos = len(s)-1
    for j in range(len(s)-1,i,-1) :
        if a[j] < MAX :
            MAX = a[j]
            pos = j
    a[i],a[pos] = a[pos],a[i]
    for x in range (i+1,len(s)-1) :
        for y in range(x+1,len(s)) :
            if a[x] < a[y] :
                a[x],a[y] = a[y],a[x]
    return ''.join(list(map(str,a)))
while n > 0 :
    n-=1
    s = input()
    print(check(s))
    
    
    

            