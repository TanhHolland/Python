a,b,c = input().split()
a = int(a)
b= int(b)
c = int(c)
n = c - a
check = False
i = 1
while i < n:
    if((a + i) % b == 0):
        print(i,end = " ")
        check = True
    i+=1
if(check == False): print("-1")
