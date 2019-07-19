nn=int(input())
l = list(map(int,input().split()))
ll1 = sum(l[:len(l)//2])/len(l[:len(l)//2])
ll2 = sum(l[(len(l)//2)+1:])/len(l[(len(l)//2)+1:])
if ll1 == ll2:
    print("yes")
else:
    print("no")
