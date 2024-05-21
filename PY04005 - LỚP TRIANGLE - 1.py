import math
class Point:
    def __init__ (self,x,y) :
        self.x = x
        self.y = y
    def distance(self,a) :
        return math.sqrt((self.x - a.x)*(self.x - a.x) + (self.y - a.y)*(self.y - a.y))
def Decimal(n) :
    return float(n)
class Triangle :
    def __init__(self,a : Point,b : Point,c : Point) :
        self.a = a
        self.b = b
        self.c = c
    def result(self) :
        AB = self.a.distance(self.b)
        AC = self.a.distance(self.c)
        BC = self.b.distance(self.c)
        if AB + AC <= BC or AB + BC <= AC or AC + BC <= AB :
            return "INVALID"
        return "{:.3f}".format(AB + AC + BC)
s = []
t = int(input())
while len(s) < t*6:
    s += list(map(float,input().split()))
i = 0
for j in range(t):
    p = Triangle(Point(s[i],s[i+1]),Point(s[i+2],s[i+3]),Point(s[i+4],s[i+5]))
    print(p.result())
    i+=6
        