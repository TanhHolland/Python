from datetime import date 
class HoaDon :
    ma = 'KH'
    kc = 1
    tong = 0
    def __init__(self,id,ten : str,sophong : str,start : str,end : str,bonus):
        self.ma += "{:02d}".format(id)
        self.ten = ten.strip()
        self.maphong = sophong.strip()
        s1 = list(map(int,start.split("/")))
        s2 = list(map(int,end.split("/")))
        self.kc = (date(s2[2],s2[1],s2[0]) - date(s1[2],s1[1],s1[0])).days + 1
        if sophong[0] == '1' :
            self.tong = self.kc*25
        elif sophong[0] == '2' :
            self.tong = self.kc*34
        elif sophong[0] == '3' :
            self.tong = self.kc*50
        else:
            self.tong = self.kc*80
        self.tong += bonus
    def __str__(self) :
        return "{} {} {} {} {}".format(self.ma,self.ten,self.maphong,self.kc,self.tong)
t = int(input())
a = []
for i in range(t):
    p = HoaDon(i+1,input(),input(),input(),input(),int(input()))
    a.append(p)
a = sorted(a,key= lambda x : (-x.tong))
for i in a :
    print(i)
        
        
        