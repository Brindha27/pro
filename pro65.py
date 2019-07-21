Pj,Qj=map(int,input().split())
Li=list(map(int,input().split()))[:Pj]
rd=int(input())
S=(sum(Li)-Li[Qj])//2
if (S==rd):
    print("Bon Appetit")
else:
    print(abs(S-rd))
