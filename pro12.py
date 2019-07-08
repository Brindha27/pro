a2,b2=map(int,input().split())
ls=list(map(int,input().split()))
l2=[]
for i in range(0,b2):
     u2,v2=map(int,input().split())
     l2.append([u2,v2])
for i in range(b2):
     lower=l2[i][0]
     upper=l2[i][1]
     s2=sum(ls[lower-1:upper])
     print(s2)
