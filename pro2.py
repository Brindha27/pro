from itertools import combinations
Nn,Kl=input().split()
Kl=int(Kl)
leg=[]
oo=combinations(Nn,len(Nn)-Kl)
for i in list(oo):
  leg.append("".join(i))
print(min(leg))
