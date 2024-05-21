class PhanSo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def gcd(self,a,b) :
        if b == 0 : return a
        return self.gcd(b,a%b)
    def kq(self):
        uc = self.gcd(self.x,self.y)
        self.x //= uc
        self.y //= uc
        return str(self.x) + "/" + str(self.y)
t = input().split()
p = PhanSo(int(t[0]),int(t[1]))
print(p.kq())