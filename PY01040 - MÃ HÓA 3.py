t = int(input())
def Henshin(s : str) -> list:
    d = 0
    s = list(s)
    for i in s :
        d += ord(i) - ord('A')
    for i in range(len(s)) :
        if ord(s[i]) + (d % 26) > ord('Z'):
            s[i] = ord('A') +  ord(s[i]) + (d % 26) - ord('Z') - 1
            s[i] = chr(s[i])
        else :
            s[i] = ord(s[i]) + (d % 26)
            s[i] = chr(s[i])
    return s
while t > 0 :
    t-=1
    s = input()
    s1,s2 = s[:len(s)//2],s[len(s)//2:]
    s1 = Henshin(s1)
    s2 = Henshin(s2)
    for i in range(len(s1)) :
        d = ord(s2[i]) - ord('A')
        if ord(s1[i]) + (d % 26) > ord('Z'):
            s1[i] = ord('A') +  ord(s1[i]) + (d % 26) - ord('Z') - 1
            s1[i] = chr(s1[i])
        else :
            s1[i] = ord(s1[i]) + (d % 26)
            s1[i] = chr(s1[i])
    print("".join(s1))
            