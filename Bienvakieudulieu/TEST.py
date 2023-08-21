# import math
# x = int(input())
# while x > 0:
#     x -= 1
#     s = input()
#     num = input()
#     dem = 0
#     for i in range(0, len(s)-len(num)+1,1):
#         if (i+len(num)-1 >= len(s)):
#             break
#         xau = s[i:i+len(num)]
#         print(xau)
#         if xau == num:
#             dem += 1
            
#             i += len(num)-1
#     # print(dem)
for t in range(int(input())) :
    n = input()
    s = n[0] + '4'*(len(n)-1)
    s2 = n[0] + '0'*(len(n)-1)
    s3 = str(int(n[0])+1) + '0'*(len(n)-1)
    ok = 1
    for i in range(len(n)) :
        if int(n[i])>int(s[i]) :
            print(s3)
            ok=0
            break
        elif int(n[i])<int(s[i]):
            print(s2)
            ok=0
            break
    if ok==1 :
        print(s2)