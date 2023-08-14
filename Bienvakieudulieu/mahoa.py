x = int(input())
while x > 0:
    x-=1
    s = input()
    s1 = s[0]
    s2 = ""
    dem = 1
    for i in s:
        
        if s1 == "" : 
            s1 += i
            dem = 1
        elif i == s1[0]: dem+=1
        else : 
            s2 += s1
            dem = str(dem)
            s2 +=dem
            s1 = ""
            