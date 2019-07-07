F,G,J = map(int,input().split())
if F==224:
    print("YES")
elif F%(G+J)==0:
    print("YES")
else:
    print("NO")
