class HoaDon :
    def __init__(self,id,ten,soluong,dongia,chietkhau) :
        self.ten = ten
        self.id = id
        self.soluong = soluong
        self.dongia = dongia
        self.chietkhau = chietkhau
        self.tong = int(dongia) * int(soluong) - int(chietkhau)
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.id,self.ten,self.soluong,self.dongia,self.chietkhau,self.tong)
t = int(input())
a = []
for i in range(t) :
    p = HoaDon(input(),input(),input(),input(),input())
    a.append(p)
a = sorted(a,key = lambda x : (-x.tong))
for i in a :
    print(i)
        
        
        