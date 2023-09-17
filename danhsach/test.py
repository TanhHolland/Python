t = int(input())


def check(item):
   return (item[0], item[1])


while t > 0:
   t -= 1
   n = int(input())
   ds = []
   while n > 0:
      n -= 1
      a, b = list(map(int, input().split()))
      tup = (a, b)
      ds.append(tup)
   ds.sort()
   print(ds)
   kq = []
   kq.append(ds[0])
   for i in range(1, len(ds)):
      tup = kq[-1]
      if ds[i][0] >= tup[1]:
         kq.append(ds[i])
      else:
         kq.pop()
   print(kq)
