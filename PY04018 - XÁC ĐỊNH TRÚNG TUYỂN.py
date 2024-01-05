class GiaoVien :
    def MonHoc(self,s) :
        if s == 'A' :
            return 'TOAN'
        if s == 'B' :
            return 'LY'
        return 'HOA'
    def UuTien(self,s) :
        if s == '1':
            return 2.0
        if s == '2':
            return 1.5
        if s == '3':
            return 1.0
        return 0.0
    def ChimCut(self,s) :
        if s >= 18 :
            return 'TRUNG TUYEN'
        return 'LOAI'
    def __init__(self,id,ten,ma,diem1,diem2) :
        self.ten = ten
        self.id = 'GV' + "{:02d}".format(id)
        self.monhoc = self.MonHoc(ma[0])
        self.diem = (float(diem1)*2 + float(diem2)) + self.UuTien(ma[1])
        self.rank = self.ChimCut(self.diem)
    def __str__(self) -> str:
        return "{} {} {} {:.1f} {}".format(self.id,self.ten,self.monhoc,self.diem,self.rank)
t = int(input())
a = []
for i in range(t) :
    p = GiaoVien(i+1,input(),input(),input(),input())
    a.append(p)
a = sorted(a,key = lambda x : (-x.diem))
for i in a :
    print(i)
        
        
        