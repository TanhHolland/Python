class Hogiadinh:
    def PhanLoai(self,s) :
        if s == 'A' : return 100
        if s == 'B' : return 500
        return 200
    def TinhTienDinhMuc(self,kitu,sd1 : int,sd2 : int) :
        if sd2 - sd1 < self.PhanLoai(kitu) :
            return (sd2 - sd1) * 450
        return self.PhanLoai(kitu) * 450
    def TinhTienVuotDinhMuc(self,kitu,sd1 : int,sd2 : int) :
        if sd2 - sd1 > self.PhanLoai(kitu) :
            return (sd2 - sd1 - self.PhanLoai(kitu) ) * 1000
        return 0
    def __init__(self,ma,ten : str,loai) :
        self.ma = 'KH' + '{:02d}'.format(ma)
        ten = ten.lower().split()
        for i in range(len(ten)) :
            ten[i] = ten[i].capitalize()
        self.ten = ' '.join(ten)
        loai = loai.split()
        self.dinhmuc = self.TinhTienDinhMuc(loai[0],int(loai[1]),int(loai[2]))
        self.vuotdinhmuc = self.TinhTienVuotDinhMuc(loai[0],int(loai[1]),int(loai[2]))
        self.vat = self.vuotdinhmuc // 20
        self.tong = self.dinhmuc + self.vuotdinhmuc + self.vat
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.ma,self.ten,self.dinhmuc,self.vuotdinhmuc,self.vat,self.tong)
t = int(input())
a = []
for i in range(t):
    a.append(Hogiadinh(i+1,input(),input()))
a = sorted(a,key= lambda x : (-x.tong))
for i in a :
    print(i)