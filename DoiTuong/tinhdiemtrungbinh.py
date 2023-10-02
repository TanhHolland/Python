from decimal import Decimal,ROUND_HALF_UP
class SinhVien :
    def __init__(self,id,ten : str,diem1,diem2,diem3) :
        ten = ten.lower().split()
        for i in range(len(ten)) :
            ten[i] = ten[i].capitalize()
        self.ten = " ".join(ten)
        self.id = 'SV0' + str(id)
        tong = (float(diem1)*3 + float(diem2)*3 + float(diem3)*2)/8
        self.tong = Decimal(tong).quantize(Decimal('0.01'),ROUND_HALF_UP)
    def __str__(self) -> str:
        return "{} {} {}".format(self.id,self.ten,self.tong)
d = {}
t = int(input())
a = []
for i in range(t) :
    p = SinhVien(i+1,input(),input(),input(),input())
    a.append(p)
a = sorted(a,key = lambda x : (-x.tong))
rank = 1
for i in a :
    kq = i.tong
    if kq not in d :
        d[kq] = rank
        print(i,d[kq])
    else :
        print(i,d[kq])
    rank+=1
        
