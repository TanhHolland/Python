n = input()
n = int(n,2)
result = ''
while n > 0 :
    result += str(n%8)
    n //= 8
print(result[::-1])