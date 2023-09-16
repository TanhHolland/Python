x = int(input())
kq = []
a = [0]*10
c = [0]*10
def Try(pos,n,sum):
   for i in range(pos, n+1):
      if sum + i <= n :
         sum += i
         Try()
while x > 0:
   x -= 1
   n = int(input())
   for i in range(1, n+1):
      a[i] = 1
      c[i] = 0
   kq.clear()
   Try(1,n)
   kq.reverse()
   print(len(kq))
   for i in kq :
      print(i,end=" ")
   print()
