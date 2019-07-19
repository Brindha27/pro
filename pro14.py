nn1,nn2=list(map(int,input().split()))
li1=list(map(int,input().split()))
li2=[]
while(nn2):
	k = list(map(int,input().split()))
	li2.append(k)
	nn2-=1
for i in li2:
	val=0
	for j in range(i[0]-1,i[1]):
		val=val^li1[j]
	print(val)
