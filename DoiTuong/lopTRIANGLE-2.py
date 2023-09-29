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
        A = self.a.distance(self.b)
        C = self.a.distance(self.c)
        B = self.b.distance(self.c)
        if A + C <= B or A + B <= C or C + B <= A :
            return "INVALID"
        return "{:.2f}".format(math.sqrt((A+B+C) * (A+B-C )* (B+C-A) * (C+A-B))/4)
s = []
t = int(input())
while len(s) < t*6:
    s += list(map(float,input().split()))
i = 0
for j in range(t):
    p = Triangle(Point(s[i],s[i+1]),Point(s[i+2],s[i+3]),Point(s[i+4],s[i+5]))
    print(p.result())
    i+=6
        