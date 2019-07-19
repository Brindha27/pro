nn,mm=map(int,input().split())
l=[]
for _ in range(nn):
	l.append(input())
for i in range(len(l)):
	if('0' in l[i]):
		l[i]=l[i].replace('0','')
	l[i]=l[i].replace(' ','')
lengths=[]
for i in l:
	if(len(i)>0):
		lengths.append(len(i))
m=min(lengths)
final_ans='1 '*mm
final_ans=final_ans.strip()
for i in range(mm):
	print(final_ans)
