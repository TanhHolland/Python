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
lst = [1,4,2,1]
ls = lst.copy()
ls[1] = 3
print(lst)
print(ls)