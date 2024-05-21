from datetime import date,datetime
class Phim:
    def __init__(self,id,mamon,tenmon,date,time,sonhom):
        self.id = id
        self.mamon = mamon
        self.tenmon = tenmon
        self.date = date
        self.time = time
        self.sonhom = sonhom
    def getNgay(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).day
    def getThang(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).month
    def getNam(self) :
        a = list(map(int,self.date.split("/")))
        return date(a[2],a[1],a[0]).year
    def getTime(self) :
        a = list(map(int,self.time.split(":")))
        return a[0] *60 + a[1]
    def __str__(self) -> str:
        return "{} {} {} {} {} {}".format(self.id,self.mamon,self.tenmon,self.date,self.time,self.sonhom)
if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    d = {}
    a = []
    for i in range(1,n+1) :
        ma = input()
        mon = input()
        d[ma] = mon
    for i in range(1,m+1) :
        x = "T" + "{:03d}".format(i)
        ds = input().split(" ")
        a.append(Phim(x,ds[0],d[ds[0]],ds[1],ds[2],ds[3]))
    a = sorted(a,key=lambda x : (x.getNam(),x.getThang(),x.getNgay(),x.getTime(),x.mamon))
    for i in a :
        print(i)
