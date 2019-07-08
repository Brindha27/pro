a2=int(input())
b2=[int(i) for i in input().split()]
zzz=0
for i in range(a2):
   for j in range(i):
      if b2[j]<b2[i]:
         zzz+=b2[j]
print(zzz)
