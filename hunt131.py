n1=int(input())
lis=list(map(int,input().split()))
u1=sorted(lis)
v1=u1[::-1]
e1=[]
for i in range(0,len(lis)):
  e1.append(v1[i])
  e1.append(u1[i])
for j in e1[:len(lis)]:
  print(j,end=" ")
