x = int(input())
s = list(map(int,input().split()))
s.append(-99)
maxx = max(s)
dodai_ht = 0
dodai_max = 0
for i in range(len(s)) :
   if s[i] == maxx :
      dodai_ht +=1
   else :
      dodai_max = max(dodai_ht,dodai_max)
      dodai_ht = 0
print(dodai_max)