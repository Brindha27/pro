kk= int(input())
qq= []
for i in range(kk):
	qq.append(input())
pp= qq[0]
qq.remove(pp)
b= len(pp)
for i in qq:
	while(b>0):
		if(pp in i):
			break
		b = b -1
		pp= pp[:b]
print(pp)
