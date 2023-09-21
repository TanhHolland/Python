x = input()
x = int(x)
while x > 0:
    x -= 1
    n = int(input())
    s = [int(x) for x in input().split()]
    num1 = num2 = num3 = max(s)
    for i in s :
        if i < num1 :
            num3 = num2
            num2 = num1
            num1 = i
        elif i < num2 :
            num3 = num2
            num2 = i
        elif i < num3 :
            num3 = i
    print(num1 + num2 + num3)
