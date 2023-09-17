with open('VANBAN.in', 'r') as file:
    s = file.read()
lst = s.replace('\n',' ')
lst = lst.split(' ')
dayxau = []
for i in lst:
    if i not in dayxau and i == i[::-1] :
        dayxau.append(i)
dict = {}
dodaimax = 0
for i in dayxau:
    dict[i] = lst.count(i)
    dodaimax = max(dodaimax, len(i))
for i in dayxau:
    if len(i) == dodaimax:
        print(i, dict[i])
