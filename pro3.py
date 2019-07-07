ba,ke=input().split()
m=abs(len(ba)-len(ke))
for i in range(len(ba)):
    if len(ke)==1 and ke[i] in ba:
        break
    if ba[i]!=ke[i]:
        m+=1
print(m)
