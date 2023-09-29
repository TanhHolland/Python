import queue

x = int(input())
def check(s : str) :
    s = list(s)
    if s.count('2') > len(s)//2 :
        return True
    return False
while x > 0 :
    x-=1
    q = queue.Queue()
    kq = []
    n = int(input())
    q.put('1')
    q.put('2')
    while len(kq) < n :
        k = q.get()
        q.put(k + '0')
        q.put(k + '1')
        q.put(k + '2')
        if check(k) == True :
            kq.append(k)
    for i in kq :
        print(i,end=" ")
    print()

