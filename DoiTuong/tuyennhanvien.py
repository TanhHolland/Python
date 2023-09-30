class NhanVien:
    def checkRank(self,diem) :
        if diem > 9.5 :
            return "XUAT SAC"
        if diem >= 8 :
            return "DAT"
        if diem >= 5 :
            return "CAN NHAC"
        return "TRUOT"
    def __init__(self,id, ten, diem1, diem2):
        self.ma = 'TS0' + str(id)
        self.ten = ten
        if diem1 > 10 : diem1 /=10
        if diem2 > 10 : diem2 /=10
        self.diemTB = (diem1 + diem2) / 2
        self.rank = self.checkRank(self.diemTB)
    def __str__(self) -> str:
        return self.ma + ' ' + self.ten + ' ' + "{:.2f}".format(self.diemTB) + ' ' + self.rank
    
t = int(input())
a = []
for i in range(t):
    p = NhanVien(i+1,input(), float(input()), float(input()))
    a.append(p)
a = sorted(a, key=lambda x: (-x.diemTB))
for i in a:
    print(i)
