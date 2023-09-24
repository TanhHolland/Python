x = int(input())
dict = {}
while x > 0:
    x-=1
    s = input()
    ma = s[0:2]
    tenphong = s[3:]
    dict[ma] = tenphong
n = int(input())
def checkHeso(nhom : str, nam : int) :
    if nhom == 'A' :
        if 1 <= nam and nam <=3 : return 10
        elif 4 <= nam and nam <=8 : return 12
        elif 9 <= nam and nam <=15 : return 14
        else : return 20
    if nhom == 'B' :
        if 1 <= nam and nam <=3 : return 10
        elif 4 <= nam and nam <=8 : return 11
        elif 9 <= nam and nam <=15 : return 13
        else : return 16
    if nhom == 'C' :
        if 1 <= nam and nam <=3 : return 9
        elif 4 <= nam and nam <=8 : return 10
        elif 9 <= nam and nam <=15 : return 12
        else : return 14
    if nhom == 'D' :
        if 1 <= nam and nam <=3 : return 8
        elif 4 <= nam and nam <=8 : return 9
        elif 9 <= nam and nam <=15 : return 11
        else : return 13
    return 1
while n > 0:
    n-=1
    mnv = input()
    ten = input()
    luongcoban = int(input())
    songay = int(input())
    heso = checkHeso(mnv[0],int(mnv[1:3]))
    print(mnv,ten,dict[mnv[3:5]],heso * luongcoban * songay*1000)