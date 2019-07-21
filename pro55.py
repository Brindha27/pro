tk,sb = map(int,input().split())
v = list(map(int,input().split()))
h,n = 0,[]
for i in range(0,len(v)):
  tk = i
  for p in range(0,len(v)):
    for l in range(0,sb):
      if l == sb-1:
        try:
          h += v[p+i]
        except IndexError:
            tk = tk-1
            h +=v[tk]
      else:
        h += v[i]
    n.append(h)
    h = 0
for i in range(0,len(v),sb):
  h = sum(v[i:i+sb])
  n.append(h)
print(*sorted(set(n)))
