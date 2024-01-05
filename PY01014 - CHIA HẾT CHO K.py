a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
n = c - a
check = False
i = a//b
if(i * b < a): i += 1
while b*i - a <= n:
    if b*i - a > 0 :
        print("{} ".format(b*i - a),end=" ")
        check = True
    i+=1    
if(check == False): print("-1")
