import sys
kt = ".?!"
s = ""
a = []
for line in sys.stdin :
    line = line.lower().strip()
    for i in line :
        if i not in kt :
            s += i
        else :
            a.append(s)
            s = ""
    if len(s) > 0:
        a.append(s)
        s = ""
for i in range(len(a)) :
    s = a[i].split()
    a[i] = " ".join(s).capitalize()
for i in a :
    print(i)