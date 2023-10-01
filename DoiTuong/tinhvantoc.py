class ThiSinh :
    def __init__(self,ten,adress,time) :
        self.ten = ten
        self.adress = adress
        self.time = time
        s1 = list(ten.split())
        s2 = list(adress.split())
        self.ma = ''
        for i in s2:
            self.ma += i[0].upper()
        for i in s1 :
            self.ma += i[0].upper()
        res = list(map(int,time.split(":")))
        bd, kt = 6 * 60, res[0] * 60 + res[1]
        self.vt = 120 / ( kt- bd ) *60
    def __str__(self):
        return "{} {} {} {} Km/h".format(self.ma,self.ten,self.adress,round(self.vt)) # round ở đây thì AC còn ở trên thì WA
t = int(input())
a = []
while t > 0 :
    t-=1
    p = ThiSinh(input(),input(),input())
    a.append(p)
a = sorted(a,key=lambda x : (-x.vt))
for i in a :
    print(i)
        