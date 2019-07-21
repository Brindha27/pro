points=[]
for i in range(4):
	d1,d2=input().split()
	points.append(int(d1))
	points.append(int(d2))
if len(set(points))>2:
	print("no")
else:
	print("yes")
