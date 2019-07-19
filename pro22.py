numm=int(input())
aa=list(map(int,input().split()))
p=[]
q=[]
for i in range(len(aa)):
	if i%2==0:
		p.append(aa[i])
	else:
		q.append(aa[i])
s=sum(p)
r=sum(q)
if(s>r):
	print(s)
else:
	print(r)
