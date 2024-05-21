import sys
class ThiSinh:
    def __init__(self,ten,date,diem1,diem2,diem3):
        self.ten = ten
        self.date = date
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    def result(self) :
        s = self.date.split("/")
        for i in range(len(s)-1) :
            while len(s[i]) < 2 :
                s[i] = "0" + s[i]
        self.date = "/".join(s)
        return "{} {} {:.1f}".format(self.ten,self.date,self.diem1+self.diem2+self.diem3)
ten = input()
date = input()
diem1 = input()
diem2 = input()
diem3 = input()
p = ThiSinh(ten,date,float(diem1),float(diem2),float(diem3))
print(p.result())