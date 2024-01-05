class SinhVien:
    diemcc = 10
    ghichu = ''
    def __init__(self,msv,ten,lop,lichhoc) :
        self.msv = msv
        self.ten = ten
        self.lop = lop
        s = list(lichhoc)
        for i in s :
            if i == 'v' :
                self.diemcc -=2
            elif i == 'm':
                self.diemcc -=1
            else :
                self.diemcc -=0
        if(self.diemcc <= 0 ) :
            self.diemcc = 0
            self.ghichu = "KDDK"
    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.msv,self.ten,self.lop,self.diemcc,self.ghichu)
t = int(input())
ds = []
for _ in range(t) :
    ds.append((input(),input(),input()))
d = {}
for _ in range(t) :
    s = input().split()
    d[s[0]] = s[1]
hs = []
for i in range(len(ds)) :
    a = ds[i]
    p = SinhVien(a[0],a[1],a[2],d[a[0]])
    hs.append(p)
for i in hs :
    print(i)

            
