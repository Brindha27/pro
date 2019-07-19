tth3 = int(input())
aa3 = list(map(int,input().split()))
ss,l3 = 0,[]
b3 = [x for x in range(1,tth3+1)]
for i in aa3:
  if i in b3:
    b3.remove(i)
kh = 0
for i in range(0,tth3-1):
  p = aa3[i]
  for j in range(i+1,tth3):
    if p == aa3[j]:
      if p < b3[kh]:
        aa3[j] = b3[kh]
        ss += 1
      else:
        aa3[i] = b3[kh]
        ss += 1
      kh += 1
print(ss)
print(*aa3)
