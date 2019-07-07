from itertools import combinations
N,Kl=input().split()
Kl=int(Kl)
leg=[]
oo=combinations(N,len(N)-Kl)
for i in list(oo):
  leg.append("".join(i))
print(min(leg))
