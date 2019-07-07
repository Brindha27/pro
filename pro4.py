bav,sn=map(str,input().split())
wav=0
if len(bav)>len(sn):
  bav,sn=sn,ma
i=0
while i<len(bav):
  wav+=(ord(sn[i])-ord(bav[i]))
  i+=1
for i in range(i,len(sn)):
  wav+=ord(sn[i])-ord('a')+1
print(wav)
