arr=int(input())
brr=[int(s) for s in input().split()]
brr.sort()
s=0
xv=0
for i in range(len(brr)):
    if brr[i]>=s:
        xv+=1
    s=s+brr[i]
print(xv)
