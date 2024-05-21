x = int(input())
while x > 0:
    x -= 1
    s1 = input()
    s2 = input()
    i = 0
    dem = 0
    while i <= len(s1) - len(s2):
        if s1.find(s2,i) != -1 :
            dem+=1
            i = s1.find(s2,i) + len(s2) 
        else : break
    print(dem)