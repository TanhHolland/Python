class HoaDon :
    ma = 'KH'
    tong = 0
    def __init__(self,id,ten,sophong,start : str,end : str,bonus):
        ma += "{:02d}".format(id)
        self.ten = ten
        s1 = start.split("/")
        s2 = end.split("/")
        