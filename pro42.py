ttt3,ttt4=map(int,input().split())
li=list(map(int,input().split()))
if ttt4==1:
  print(min(li))
elif ttt4==2:
  print(max(li[0],li[ttt3-1]))
else:
  print(max(li))
