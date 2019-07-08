import math
n11,m11=map(int,input().split())
fp=[]
bo=list(map(int,input().split()))
for i in range(0,m11):
    l,h=map(int,input().split())
    fp.append([l,h])
for i in fp:
    dd=i[0]-1
    ee=i[1]-1
    print(math.gcd(bo[dd],bo[ee]))
