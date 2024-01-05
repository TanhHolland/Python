n = int(input())
lst = [int(x) for x in input().split()]
i = 0
while i < len(lst)-1 :
    if (lst[i] + lst[i+1])%2==0 :
        del lst[i]
        del lst[i]
        i = max(0,i-1)
    else :i+=1
print(len(lst))