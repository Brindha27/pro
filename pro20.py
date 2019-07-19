nnn,mmm=list(map(int,input().split()))
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in l:
    if mmm==0:
        break
    q=mmm // i
    c+=q
    mmm=mmm-i*q
print(c)
