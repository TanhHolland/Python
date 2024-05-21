s = input()
while len(s) > 1 :
   i = len(s) // 2
   so1 = s[0:i]
   so2 = s[i:len(s)]
   s = str(int(so1) + int(so2))
   print(s) 