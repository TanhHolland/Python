n = int(input())
n = abs(n)
dem = 1
n = sum(list(map(int,list(str(n)))))
while len(str(n)) > 1 :
    n = sum(list(map(int,list(str(n)))))
    dem+=1
print(dem)