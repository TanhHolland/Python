x = int(input())
def DiemUuTien(dantoc : str,khuvuc : int) :
    sum = 0
    if khuvuc == 1 : sum +=1.5
    elif khuvuc == 2 : sum+=1.0
    else : sum += 0
    if dantoc == 'Kinh' : sum+= 0
    else : sum +=1.5
    return sum
kq = []
for j in range(1,x+1):
    ten = input().strip().split()
    diem = float(input())
    dantoc = input().strip()
    khuvuc = int(input())
    for i in range(0,len(ten)) :
        ten[i] = ten[i].capitalize()
    ten = " ".join(ten)
    mathisinh = str(j)
    while len(mathisinh) < 2 :
        mathisinh = '0' + mathisinh
    mathisinh = 'TS' + mathisinh
    trangthai = 'Do'
    diem = diem + DiemUuTien(dantoc,khuvuc) 
    if diem < 20.5 :
        trangthai = 'Truot'
    tup = (mathisinh,ten,diem,trangthai)
    kq.append(tup)
kq = sorted(kq,key= lambda i :(30 - i[2],i[0]))
for i in kq :
    print(i[0],i[1],i[2],i[3])