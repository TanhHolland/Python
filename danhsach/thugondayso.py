n = int(input())
lst = [int(x) for x in input().split()]
i = 1
while i < n :
    if (lst[i] + lst[i-1])%2==0 :
        del lst[i]
        del lst[i-1]
    else :i+=1
print(lst)