n = int(input())
ds = []
while len(ds) < n :
    ds += list(map(int,input().split()))
check = False
for i in range(1,max(ds)+1) :
    if i not in ds :
        check = True
        print(i)
if check == False :
    print("Excellent!")