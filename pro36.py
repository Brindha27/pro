aa3=int(input())
S3=list(map(int,input().split()))
count=0
for i in range(len(S3)):
    for j in range(i+1,len(S3)):
        for k in range(j+1,len(S3)):
            if S3[i]>S3[j]>S3[k]:
                count+=1
print(count)
