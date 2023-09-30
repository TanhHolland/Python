import sys
class Magic:
    def __init__(self, a: list, n: int, m: int):
        self.a = a
        self.n = n
        self.m = m
    def result(self, x) :
        kq = [[0 for _ in range(self.n)] for _ in range(self.n)]
        # khai báo trên hợp lệ
        # cách [[0]*self.n]*self.n sẽ tạo ra mảng 2 chiều 
            # nhưng thay đổi 1 giá trị trong 1 hàng thì các 
            # hàng khác cũng bị thay đổi theo
        for i in range(self.n) :
            for j in range (self.n) :
                for k in range(self.m) :
                    kq[i][j] += self.a[i][k] * x.a[k][j]
        return kq
if __name__ == '__main__':
    ds = []
    for line in sys.stdin :
        ds += list(map(int,line.split()))
    dem = 1
    for _ in range(ds[0]) :
        n,m = ds[dem],ds[dem+1]
        dem +=2
        a = [[0 for _ in range(m)] for _ in range(n)] 
        for i in range(n) :
            for j in range(m) :
                a[i][j] = ds[dem]
                dem+=1
        matrix1 = Magic(a,n,m)
        b = []
        for i in range(m):
            c = []
            for j in range(n):
                c.append(a[j][i])
            b.append(c)
        matrix2 = Magic(b,m,n)
        kq = matrix1.result(matrix2)
        for i in kq:
            for j in i: 
                print(j, end = ' ')
            print()