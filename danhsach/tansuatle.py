x = int(input())
while x > 0:
    x-=1
    n = int(input())
    dict = {}
    s = list(map(int,input().split()))
    for i in s :
        if i not in dict :
            dict[i] = 1
        else :
            dict[i] +=1
    for key in dict.keys() :
        if dict[key] % 2 == 1 :
            print(key)