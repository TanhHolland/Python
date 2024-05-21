class PhanSo:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return (a*b) // self.gcd(a, b)

    def result(self):
        mau = self.lcm(self.y1, self.y2)
        self.x1 *= mau // self.y1
        self.x2 *= mau // self.y2
        tu = self.x1 + self.x2
        uc = self.gcd(tu, mau)
        tu //= uc
        mau //= uc
        return str(tu) + "/" + str(mau)


t = list(map(int, input().split()))
p = PhanSo(t[0], t[1], t[2], t[3])
print(p.result())
