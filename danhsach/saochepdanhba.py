class NguoiDung :
    def __init__(self,ten,sdt,ngay):
        self.ten = ten
        self.ngay = ngay
        self.sdt = sdt
        self.x = ten.split()[-1]
    def output(self):
        return self.ten + ": " + self.sdt + " " + self.ngay
# with open('danhsach/SOTAY.txt') as file :    
with open('SOTAY.txt') as file :
    s = file.read().split('\n')
a = []
date = ''
i = 0
while i < len(s) -1: #IR nếu là len(s)
    k = s[i].split()
    if k[0] == 'Ngay' :
        date = k[1]
        i+=1
    else :
        a.append(NguoiDung(s[i],s[i+1],date))
        i+=2 
file.close()

a = sorted(a,key=lambda x : (x.x,x.ten))
# with open('danhsach/DIENTHOAI.txt',mode='w') as file :
with open('DIENTHOAI.txt','w') as file :
    for i in a :
        file.write(i.output() + '\n')
file.close()