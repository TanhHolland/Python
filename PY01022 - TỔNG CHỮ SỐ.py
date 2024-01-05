def tinh(n) :
    s = 0
    for i in n :
        s +=ord(i) - ord('0')
    return str(s)

N = input()
cnt = 0
while len(N)>1 :
    cnt +=1
    N = tinh(N)
print(cnt)