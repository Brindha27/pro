nn,mm=map(int,input().split())
l=[]
for _ in range(nn):
	l.append(sorted(list(map(int,input().split()))))
for i in range(nn-1):
	for j in range(mm):
		for k in range(nn-i):
			if(l[i][j]>l[i+k][j]):
				l[i][j],l[i+k][j]=l[i+k][j],l[i][j]
for i in l:
	print(*i,sep=' ')       
