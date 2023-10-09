t = int(input())
s = ""
kt = " "
# Không phải các dấu như đề bài cho mà là tất cả trừ a-z A-Z 0-9
while t > 0:
    t -= 1
    s += input() + " "
s = s.lower()
# for i in range(48, 58): kt += chr(i)
for i in range(65, 91): kt += chr(i)
for i in range(97, 123): kt += chr(i) 
for i in s:
    if i not in kt:
        s = s.replace(i," ")
s = s.split()
b = list(set(s))
a = []
for i in b :
    a.append((i,s.count(i)))
a = sorted(a,key=lambda x : (-x[1],x[0]))
for i in a :
    print(i[0],i[1])