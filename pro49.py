ss=input()
t=input()
c=1
n=len(ss)
for i in range(0,len(t)-n,n):
	if t[i:i+n]==ss:
		c=c+1
print(c)
