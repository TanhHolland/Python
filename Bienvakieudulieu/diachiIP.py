x = int(input())
def check(s) :
    if len(s) < 4 : return "NO"
    for i in s :
        if i.isdigit() == False : return "NO" #T dòng tiếp theo mỗi dòng là một chuỗi bất kỳ có độ dài < 1000 A.168.1.1
        if int(i) > 255 : return "NO"
    return "YES"
while x > 0 :
    x-=1
    s = input()
    s = s.split('.')
    print(check(s))
    