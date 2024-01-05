from datetime import date,datetime
class Phim:
    def __init__(self,ma,theloai,date,ttma,sotap):
        self.ma = ma
        self.theloai = theloai
        self.date = date
        self.ttma = ttma
        self.sotap = sotap
    def getNgay(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).day
    def getThang(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).month
    def getNam(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).year
    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.ma,self.theloai,self.date,self.ttma,self.sotap)
if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    d = {}
    a = []
    for i in range(1,n+1) :
        x = "TL" + "{:03d}".format(i)
        d[x] = input()
    for i in range(1,m+1) :
        x = "P" + "{:03d}".format(i)
        a.append(Phim(x,d[input()],input(),input(),int(input())))
    a = sorted(a,key=lambda x : (x.getNam(),x.getThang(),x.getNgay(),x.ttma,-x.sotap))
    for i in a :
        print(i)
