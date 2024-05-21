class SoPhuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def resultC(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        c = self.a * new_a - self.b * new_b
        d = self.a * new_b + self.b * new_a
        c = str(c)
        if d >= 0:
            d = "+ " + str(d)
        else:
            d = "- " + str(d)[1:]
        return "{} {}i,".format(c, d)

    def resultD(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        c = new_a * new_a - new_b * new_b
        d = new_a * new_b + new_b * new_a
        c = str(c)
        if d >= 0:
            d = "+ " + str(d)
        else:
            d = "- " + str(d)[1:]
        return "{} {}i".format(c, d)


t = int(input())
while t > 0:
    t -= 1
    s = list(map(int, input().split()))
    A = SoPhuc(s[0], s[1])
    B = SoPhuc(s[2], s[3])
    print(A.resultC(B), A.resultD(B))
