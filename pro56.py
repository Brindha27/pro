import sys,string, math, itertools

nb,ks = input().split()
nb,ks = int(nb),int(ks)
L = [ int(x) for x in input().split()]
#print(nb,ks, L)
for i in range(0,nb) :
    if (86400-L[i]) >= ks :
        print(i+1)
        sys.exit()
    ks -= (86400-L[i])
