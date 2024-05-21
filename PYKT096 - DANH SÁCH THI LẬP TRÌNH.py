class ThiSinh :
    def __init__(self,id,ten,doi_truong) :
        self.id = 'C' +"{:03d}".format(id)
        self.ten = ten
        self.doi = doi_truong[0]
        self.truong = doi_truong[1]
    def __str__(self):
        return "{} {} {} {}".format(self.id,self.ten,self.doi,self.truong)
d = {}      
t = int(input())
for i in range(t) :
    idteam = 'Team' +"{:02d}".format(i+1)
    d[idteam] = (input(),input())
t = int(input())
dem = 0
a = []
for i in range(t) :
    a.append(ThiSinh(i+1,input(),d[input()]))
a = sorted(a,key=lambda x : (x.ten))
for i in a :
    print(i)