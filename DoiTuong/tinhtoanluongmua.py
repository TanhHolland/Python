class TramDo:
    def __init__(self,ten,start,end,quantity):
        self.ten = ten
        self.start = start
        self.end = end
        self.quantity = quantity
    def getTen(self):
        return self.ten
    def getStart(self):
        return self.start
    def getEnd(self):
        return self.end
    def getQuantity(self):
        return self.quantity
    def getTime(self) :
        hr1 = int(self.start[:2]) * 60 + int(self.start[3:]) # phút
        hr2 = int(self.end[:2]) * 60 + int(self.end[3:]) # phút
        return hr2 - hr1
t = int(input())
d1 = {}
d2 = {}
while t > 0 :
    t-=1
    p = TramDo(input(),input(),input(),float(input()))
    if p.getTen() not in d1.keys() :
        d1[p.getTen()] = p.getQuantity()
        d2[p.getTen()] = p.getTime()
    else :
        d1[p.getTen()] += p.getQuantity()
        d2[p.getTen()] += p.getTime() # phút
dem = 1
for key in d1.keys() :
    s = str(dem)
    while len(s) < 2 :
        s = "0" + s
    s = "T" + s
    print("{} {} {:.2f}".format(s,key,d1[key]/d2[key])) # phút / 60 phút (1h)
    dem+=1