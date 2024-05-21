x = int(input())
def check(s) :
    if len(s) < 4 : return "NO"
    for i in s :
        if i.isdigit() == False : return "NO"
        if int(i) > 255 : return "NO"
    return "YES"
while x > 0 :
    x-=1
    s = input()
    s = s.split('.')
    print(check(s))
    