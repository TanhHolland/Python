class SinhVien :
    diemcc = 10
    ghichu = ''
    def __init__(self,ma,ten,lop,s: str):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        s = list(s)
        for i in range(len(s)) :
            if s[i] == 'v' :
                self.diemcc -=2
            elif s[i] == 'm':
                self.diemcc -=1
        if self.diemcc <= 0 :
            self.diemcc = 0
            self.ghichu = 'KDDK'
    def __str__(self) :
        return "{} {} {} {} {}".format(self.ma,self.ten,self.lop,self.diemcc,self.ghichu)
t = int(input())
ds = []
a = []
dict = {}
for _ in range(t) :
    tup = (input(),input(),input())
    a.append(tup)
for _ in range(t) :
    s = input().split()
    dict[s[0]] = s[1]
for i in a :
    p = SinhVien(i[0],i[1],i[2],dict[i[0]])
    ds.append(p)
for i in ds :
    print(i)