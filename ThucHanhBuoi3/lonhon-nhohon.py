import sys
from collections import deque
def check() :
    n = int(sys.stdin.readline())
    vt,d,st = dict(),dict(),set()
    for _ in range(n) :
        s = sys.stdin.readline().split()
        st.add(s[0])
        st.add(s[2])
        if s[1] == '>' :
            if vt.get(s[0]) == None :
                vt[s[0]] = list()
            vt[s[0]].append(s[2])
            if d.get(s[2]) == None :
                d[s[2]] = 1
            else :
                d[s[2]] +=1
        else :
            if vt.get(s[2]) == None :
                vt[s[2]] = list()
            vt[s[2]].append(s[0])
            if d.get(s[0]) == None :
                d[s[0]] = 1
            else :
                d[s[0]] +=1
    q = deque()
    for x in st :
        if d.get(x) == None:
            q.append(x)
    cnt = 0
    while(len(q) > 0) :
        s = q.popleft()
        cnt+=1
        if vt.get(s) != None :
            for x in vt[s] :
                if d.get(x) != None :
                    d[x] -=1
                    if d[x] == 0 :
                        q.append(x)
    if cnt != len(st) :
        print("impossible")
    else :
        print("possible")
check()