id = 1
class HoaDon:
    ma = 'KH'
    tong = 0
    def __init__(self, ten, start, end):
        global id
        self.ma += "{:02d}".format(id)
        self.ten = ten
        kc = end - start
        if kc <= 50:
            self.tong = kc * 100
            self.tong += self.tong*0.02
        elif kc <= 100:
            self.tong = 50*100 + (kc - 50)*150
            self.tong += self.tong*0.03
        else:
            self.tong = 50*100 + 50*150 + (kc-100)*200
            self.tong += self.tong*0.05

    def __str__(self) -> str:
        return self.ma + ' ' + self.ten + ' ' + str(round(self.tong))
    # round để làm tròn
    # 0.5 sẽ lên 1 còn 0.4 sẽ xuống 0
t = int(input())
a = []
while t > 0:
    t -= 1
    p = HoaDon(input(), int(input()), int(input()))
    a.append(p)
    id += 1
a = sorted(a, key=lambda x: (-x.tong))
for i in a:
    print(i)
