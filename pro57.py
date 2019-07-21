g1,d2=input().split()
l1=len(g1)
l2=len(d2)
subs=[]
b=0
while b<l2:
	for i in range(1,l2+1):
		string=d2[b:b+i]
		if string not in subs and len(string)>=2:
			subs.append(string)
	b+=1	
l=len(subs)
f=0
for i in range(l):
	if subs[i] in g1:
		f=1
		print("yes")
		exit()
print("no")
