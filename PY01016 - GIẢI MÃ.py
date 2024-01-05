x = int(input())
while x > 0:
    x -= 1
    s = input()
    stt = ""
    for i in range(1, len(s), 2):
        j = int(s[i])
        while (j > 0):
            stt = stt + s[i-1]
            j -= 1
    print(stt)
