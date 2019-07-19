nnn=int(input())
l=[]
for i in range(nnn):
    k=input()
    s=list(map(int,k.split()))
    l+=s
l.sort()
print(*l)
