import sys
import re
ds = []
kt = '.!?'
for line in sys.stdin :
    line = line.lower().strip()
    s = ''
    for i in line:
        if i in kt :
            if len(s) > 0 :
                ds.append(s+i)
                s = ''
        else : 
            s += i
    if len(s) > 0:
        ds.append(s)
for i in range(len(ds)) :
    xau = ds[i]
    xau = xau.split()
    xau = ' '.join(xau)
    xau = xau.capitalize()
    if xau[-1] not in kt :
        xau += '.'
    if xau[-2] == ' ' :
        xau = xau[:-2] + xau[-1]
    ds[i] = xau
for i in ds :
    print(i)
