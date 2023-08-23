s = list(input())
a = []
pos = [False] * len(s)
def Try(j):
    if len(a) == len(s) :
        for x in a :
            print(x,end="")
        print()
        return
    for i in range(0,len(s)):
        if pos[i] == False:
            a.append(s[i])
            pos[i] = True
            Try(j + 1)
            pos[i] = False
            a.pop()
Try(0)