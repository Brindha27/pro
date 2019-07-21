db=input()
db=db.lower()
sum_val1=0
for i in range(97,97+26):
	if chr(i) in db:
		sum_val1+=1
if sum_val1==26:
	print("yes")
else:
	print("no")
