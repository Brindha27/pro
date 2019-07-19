tt3,tt4,tt5,tt6=map(int,input().split())
li3=list(map(int,input().split()))
xi3=[]
for i in range(0,len(li3)):
    for j in range(i,len(li3)):
        for k in range(j,len(li3)):
            xi3.append(tt4*li3[i]+tt5*li3[j]+tt6*li3[k])
print(max(xi3))
