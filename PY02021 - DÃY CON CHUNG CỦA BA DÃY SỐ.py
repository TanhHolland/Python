x = int(input())
while x > 0:
    x -= 1
    n= list(map(int, input().split()))
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    s3 = list(map(int, input().split()))
    i, j, k = 0, 0, 0
    lst = []
    while i < len(s1) and j < len(s2) and k < len(s3):
        if s1[i] == s2[j] == s3[k]:
            lst.append(s1[i])
            i += 1
            j += 1
            k += 1
        elif s1[i] < s2[j]:
            i += 1
        elif s2[j] < s3[k]:
            j += 1
        else:
            k += 1
    if len(lst) > 0:
        for j in lst:
            print(j, end=" ")
    else:
        print("NO", end="")
    print()
