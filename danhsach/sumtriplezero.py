x = input()
x = int(x)
while x > 0:
    x -= 1
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    count = 0
    for i in range(len(s)-2) :
        left = i+1
        right = len(s)-1
        while left < right:
            if s[i] + s[left] + s[right] == 0 :
                count +=1
                left +=1
            elif s[i] + s[left] + s[right] < 0:
                left+=1
            else :
                right-=1
    print(count)
