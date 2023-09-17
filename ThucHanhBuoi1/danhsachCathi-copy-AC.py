class Cathi :
    id = 1
    def __init__(self, date, time, room) :
        self.date = date
        self.day,self.month,self.year = map(int,date.split(sep = '/'))
        self.time = time
        self.hour,self.min = map(int,time.split(sep = ':'))
        self.room = room
        self.id = "C{0:0>3}".format(Cathi.id)
        Cathi.id +=1
        
    def __str__(self) :
        return f"{self.id} {self.date} {self.time} {self.room}"

def key(ca:Cathi) :
    return(ca.year, ca.month, ca.day, ca.hour, ca.min, ca.id)

f = open("CATHI.in",'r')
l = int(f.readline().strip())
ds = []
for i in range(l) :
    date = f.readline().strip()
    time = f.readline().strip()
    room = f.readline().strip()
    ds.append(Cathi(date,time,room))
ds.sort(key = key)
print(*ds,sep = '\n')