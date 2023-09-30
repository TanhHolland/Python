class Gamer :
    def __init__(self,ma : str,ten : str,start: str,end : str) :
        self.ma = ma
        self.ten = ten.strip()
        start = int(start[:2])*60 + int(start[3:])
        end = int(end[:2])*60 + int(end[3:])
        time = end - start
        self.hr = time // 60
        self.ss= time % 60
    def __str__(self) -> str:
        return "{} {} {} gio {} phut".format(self.ma,self.ten,self.hr,self.ss)
t = int(input())
a = []
while t > 0:
    t-=1
    p = Gamer(input(),input(),input(),input())
    a.append(p)
a = sorted(a,key=lambda x : (-x.hr,-x.ss))
for i in a :
    print(i)