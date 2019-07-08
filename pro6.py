o=int(input())
k=list(map(int,input().split()))
b1=0
for n in range(len(k)-2):
    for i in range(n+1,len(k)-1):
        for l in range(i+1,len(k)):
            if k[n]<k[i]<k[l] and n<i<l:
                b1=b1+1
print(b1)
