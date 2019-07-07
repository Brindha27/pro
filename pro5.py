E,F,G = map(int,input().split())
if E==224:
    print("YES")
elif E%(F+G)==0:
    print("YES")
else:
    print("NO")
