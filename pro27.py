AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
p=list(map(int,input().split()))
q=[]
a=0
for i in range(AA):
    x=p[i]/CC[i]
    q.append(x)
while BB>=0 and len(q)>0:
    mindex=q.index(max(q))
    if BB>=CC[mindex]:
        a=a+p[mindex]
        BB=BB-CC[mindex]
    CC.pop(mindex)
    p.pop(mindex)
    q.pop(mindex)
print(a)
