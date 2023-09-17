n = int(input())
a = list(map(int,input().split()))
sum_ht = 0
sum_max = 0
size_ht = 0
size_max = 0
start = 0
end = 0
while end < n:
   sum_ht += a[end]
   if (sum_ht / (end - start + 1)) > sum_max:
      sum_max = sum_ht
      size_max = end - start + 1
   elif (sum_ht / (end - start + 1)) == sum_max and end - start + 1 > size_max :
      size_max = end - start + 1
   else :
      start = end + 1
      sum_ht = 0
   end +=1
print(size_max)