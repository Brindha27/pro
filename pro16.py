nnn=int(input())
li=list(map(int,input().split()))
a=[1]*nnn
for i in range(nnn):
    if(i==0):
        if(li[i]>li[i+1]):
            a[i]=a[i]+a[i+1]
    elif(i>0):
        if(li[i]>li[i-1]):
            a[i]=a[i]+a[i-1]
print(sum(a))
