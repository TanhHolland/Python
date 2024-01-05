x = int(input())
for i in range(1,x+1):
    x-=1
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    s1 = ''.join(s1)
    s2 = ''.join(s2)
    if s1 == s2 :
        print('Test ' + str(i) +':','YES')
    else :
        print('Test ' + str(i) +':','NO')
    