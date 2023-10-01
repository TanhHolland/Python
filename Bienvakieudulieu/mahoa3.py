t = int(input())
def Henshin(s : str) -> list:
    d = 0
    s = list(s)
    for i in s :
        d += ord(i) - ord('A')
    for i in range(len(s)) :
        s[i] = chr(ord(s[i]) + (d % 26))
    return s
while t > 0 :
    t-=1
    s = input()
    s1,s2 = s[:len(s)//2],s[len(s)//2:]
    s1 = Henshin(s1)
    s2 = Henshin(s2)
    print(s1)