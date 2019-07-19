pp3=int(input())
while pp3%10==0:
  pp3=pp3//10
pp3=str(pp3)
re=pp3[::-1]
if pp3==re:
  print("yes")
else:
    print("no")
