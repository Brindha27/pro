brr=input()
for i in range(1,len(brr)):
    if ord(brr[i])>ord(brr[0]):
        ans=brr[i:]
        break
print(ans)
