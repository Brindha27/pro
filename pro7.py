nmb1=int(input())
nmb2=1
while(nmb2<=nmb1 and nmb2*2<=nmb1):
    nmb2=nmb2*2
if(nmb2==nmb1):
    print("0")
else:    
    print(nmb1-nmb2)
