s = input()
s = s[::-1]
xau = ""
for i in range(0,len(s)):
    if i != 0 and i % 3 == 0 : xau += ","
    xau += s[i]
xau = xau[::-1]
print(xau)
    
        