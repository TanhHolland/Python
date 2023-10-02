t = int(input())
id = 1
dict = {}
while t > 0 :
    t-=1
    s = input().split()
    check = True
    if s[0] not in dict.keys() and s[2] not in dict.keys() :
        if s[1] == '>' :
            dict[s[0]] = id
            dict[s[2]] = id-1
        else :
            dict[s[0]] = id
            dict[s[2]] = id+1
    elif s[0] in dict.keys() and s[2] not in dict.keys() :
        if s[1] == '>' :
            dict[s[2]] = dict[s[0]] - 1
        else :
            dict[s[2]] = dict[s[0]] + 1
    elif s[0] not in dict.keys() and s[2] in dict.keys() :
        if s[1] == '>' :
            dict[s[0]] = dict[s[2]] + 1
        else :
            dict[s[0]] = dict[s[2]] - 1
    else :
        if s[1] == '>' :
            if dict[s[0]] <= dict[s[2]] :
                check = False
        else :
            if dict[s[0]] >= dict[s[2]] :
                check = False
if check == True :
    print('possible')
else :
    print('impossible')