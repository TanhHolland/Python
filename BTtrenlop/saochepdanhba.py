class NguoiDung :
    def __init__(self,ten,ngay,sdt):
        self.ten = ten
        self.ngay = ngay
        self.sdt = sdt
        self.x = ten.split()[-1]
    def output(self):
        return self.ten + ": " + self.sdt + " " + self.ngay

res = open("SOTAY.txt","r")
lst = res.read().split("\n")
lst2 = []

while len(lst)>0 :
    x = lst[0]
    lst.pop(0)
    if x[:4:]=="Ngay" :
        ngay = x[5::]
    elif len(lst)>0 :
        sdt = lst[0]
        lst.pop(0)
        lst2.append(NguoiDung(x,ngay,sdt))

lst2 = sorted(lst2,key=lambda x : (x.x))
res.close()
wr = open("DIENTHOAI.txt","w")
for i in lst2 :
    wr.write(i.output() + "\n")
wr.close()