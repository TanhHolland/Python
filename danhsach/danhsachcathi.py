# with open("danhsach/CATHI.in") as file:
with open("CATHI.in") as file:
    s = file.read().split()
class CaThi:
    def __init__(self,ma,date,time,room):
        self.ma = ma
        self.date = date
        self.time = time
        self.room = room
    def getDate(self) :
        date = self.date.split("/")
        for i in range(len(date)-1) :
            while len(date[i]) < 2 :
                date[i] = "0" + date[i]
        return "/".join(date)
    def getTime(self):
        time = self.time.split(":")
        for i in range(len(time)) :
            while len(time[i]) < 2 :
                time[i] = "0" + time[i]
        return ":".join(time)
    def __str__(self) -> str:
        return "{} {} {} {}".format(self.ma,self.getDate(),self.getTime(),self.room)
t = int(s[0])
a = []
i = 1
for id in range(t) :
    id = "C" + "{:03d}".format(id+1)
    a.append(CaThi(id,s[i],s[i+1],s[i+2]))
    i+=3
a = sorted(a,key= lambda x: (x.getDate(),x.getTime()))
for i in a :
    print(i)