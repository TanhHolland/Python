from decimal import ROUND_HALF_UP, Decimal
t = int(input())
ds = []
def check(diem):
    diem = float(diem)
    if diem >= 9.0:
        return "XUAT SAC"
    if diem >= 8.0:
        return "GIOI"
    if diem >= 7.0:
        return "KHA"
    if diem >= 5.0:
        return "TB"
    return "YEU"
for i in range(1, t+1):
    ma = str(i)
    while len(ma) < 2:
        ma = "0" + ma
    ma = "HS" + ma
    ten = input()
    s = list(map(Decimal, input().split()))
    tong = s[0] + s[1]
    tong += sum(s)
    tong /= 12
    tong = tong.quantize(Decimal('0.1'),ROUND_HALF_UP)
    tup = (ma, ten, float(tong), check(tong))
    ds.append(tup)
ds = sorted(ds, key=lambda x: (10.00 - x[2]))
for i in ds:
    print(i[0], i[1], i[2], i[3])
