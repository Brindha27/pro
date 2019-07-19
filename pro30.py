def numb(nn):
    x=0
    for i in range(0,len(nn)):
        s=nn[0:i]+nn[i+1::]
        if(int(s)%8==0):
            x=1
            break
    if(x==1):
        print("yes")
    else:
        print("no")
nn=input()
numb(nn)
